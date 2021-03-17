import pandas

# Windmessdaten Frick 2007 - 2009, v [m/s] 50 Meter über Grund
data = pandas.read_excel("data/winddaten.xls")

# calculates timestamps in proper format
date_time = pandas.to_datetime(
    data[["year", "month", "day", "hour"]]
) - pandas.to_timedelta("1 hour")

# drops unneeded values
data = data.drop(["year", "month", "day", "hour"], axis=1)

# adds DateTime index
data["DateTime"] = date_time
data = data.set_index("DateTime")

# saves file
data.to_pickle("data/winddaten.pkl")