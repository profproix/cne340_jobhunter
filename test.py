import datetime as dt

current_date = dt.datetime.now()
post_date = dt.datetime.strptime("2024-02-07T00:51:00", "%Y-%m-%dT%H:%M:%S")


print(current_date.day)
print(post_date.day)