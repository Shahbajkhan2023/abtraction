# import datetime

# datetime_object = datetime.datetime.now()
# print(datetime_object)




# import datetime

# date_object = datetime.date.today()
# print(date_object)



# import datetime

# d = datetime.date(2019, 4, 13)
# print(d)


# from datetime import datetime


# print(datetime.now())



# from datetime import date
# print(date.today())



# from datetime import date
# print(date.today().year)



# from datetime import time
# print(time())
# print(time(12, 12, 12))
# print(time(hour=2, minute=12, second=14))



# from datetime import time
# a = time(12, 12, 12, 12)
# print(a.hour)
# print(a.minute)
# print(a.second)
# print(a.microsecond)



# from datetime import datetime
# print(datetime(12, 13, 1))
# print(datetime())


# from datetime import datetime
# a = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print(a.year. a.month, a.hour, a.minute, a.tiemstamp())



# from datetime import datetime, date
# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)
# t3 = t1 - t2
# print(t3)

# t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 32)
# t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 44)
# t6 = t4 - t5
# print(t6)





# from datetime import timedelta

# t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
# t3 = t1 = t2




# from datetime import datetime
# now = datetime.now()

# t = now.strftime("%H:%M:%S")
# print(t)

# s1 = now.strftime('%m/%d/%y, %H:%M:%S')
# print(s1)


# from datetime import datetime

# date_string = '21 June, 2018'
# print('Date_string =', date_string)

# data_object = datetime.strptime(date_string, '%d %B, %Y')
# print(data_object)




# from datetime import datetime
# print(datetime.now())


# from datetime import datetime
# print(datetime.now())


# from datetime import date
# print(date.today())





# from datetime import datetime
# print(datetime.now())

# from datetime import date
# print(date.today())





# from datetime import date
# print(date.fromtimestamp(1231231221))





# from datetime import datetime
# print(datetime.now())


# from datetime import date
# print(date.today())


# from datetime import date
# print(date.today().month)
# print(date.today().year)
# print(date.today().day)






# from datetime import time
# print(time())
# print(time(11, 34, 56))
# print(time(hour=11, minute=34, second=56))



# from datetime import datetime
# print(datetime.now())

# from datetime import date
# print(date.today())


# from datetime import date
# print(date.today().year)
# print(date.today().month)
# print(date.today().day)



# from datetime import time 
# print(time())
# print(time(12, 12, 12))
# print(time(hour=12, minute=12, second=12))
# a = time(hour=12, minute= 12, second= 12)
# print(a.hour, a.minute, a.second)


# from datetime import datetime

# a = datetime(2018, 12, 1, 12, 12, 12)
# print(a)
# print(a.day, a.year, a.month)




# from datetime import date, datetime

# t1 = date(year=2012, month=11, day = 12)
# t2 = date(year=2018, month= 12, day= 11)
# print(t1-t2)




# from datetime import datetime

# now = datetime.now()
# print(now)
# print(now.strftime('%d/%m/%Y, %H/%M/%S'))




# from datetime import datetime
# now = datetime.now()

# print(now.strftime('%Y'))
# print(now.strftime('%m'))
# print(now.strftime('%d'))




# from datetime import datetime

# timestamp = 1528797322
# date_time = datetime.fromtimestamp(timestamp)
# print(date_time)






# from datetime import datetime

# date_string = '21 June, 2018'
# print(datetime.strptime(date_string, "%d %B, %Y"))



# from datetime import datetime

# date_string = '12/11/2018 09:15:32'
# dt_object1 = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S" )
# print(dt_object1)



# from datetime import date
# print(date.today())

# print(date.today().strftime('%d/%m/%Y'))




# from datetime import datetime
# print(datetime.now())
# print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))



# import time 

# t = time.localtime()
# current_time = time.strftime("%H:%M:%S")
# print(current_time)




# import time
# second  = time.time()
# print(second)

# second = 1721294598.5304105
# local_time = time.ctime(second)
# print(local_time)



# import time
# print('This is printed immediately')
# time.sleep(2.4)
# print('This is printed after 2.4 seconds')


# import time

# result = time.localtime(1545925769)
# print(result)
# print(result.tm_year)
# print(result.tm_hour)


# result = time.gmtime(1545925769)
# print(result)
# print(result.tm_year)
# print(result.tm_hour)





# import time
# print('Printed immdediately.')
# time.sleep(2.4)
# print('Printed after 2.4 seconds.')



# import time
# print('Printed immediately')
# time.sleep(2.4)
# print('Printed after 2.4 seconds.')



# import time

# while True:
#     localtime = time.localtime()
#     result = time.strftime('%I:%M:%S %p', localtime)
#     print(result)
#     time.sleep(1)



# import time
# second = time.time()
# print(second)


# import time
# second = time.time()
# print(second)


# import time

# second = time.time()
# print(time.ctime(second))

# import time 

# result = time.localtime(15459225769)
# print(result)
# print(result.tm_year)
# print(result.tm_hour)


# import time

# result = time.localtime(1545925769)
# print(result)
# print(result.tm_year)
# print(result.tm_hour)



# import time

# result = time.gmtime(1545925769)
# print(result)








# import time

# t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

# result = time.asctime(t)
# print(result)


# import time
# second = time.time()
# print(second)


# import time
# second = time.time()
# local_time = time.ctime(second)
# print(local_time)


# import time
# result = time.localtime(1545925769)
# print(result)


# import gtime
# result = time.gtime(1545925769)
# print(result)



# from datetime import datetime

# timestamp = 1545730073
# dt_object = datetime.fromtimestamp(timestamp)

# print(dt_object)



# from datetime import datetime
# timestamp = 15


# from datetime import datetime

# timestamp = 123123123
# dt_object = datetime.fromtimestamp(timestamp)
# print()



# from datetime import datetime 

# print(datetime.now())
# print(datetime.timestamp(datetime.now()))



# from datetime import datetime

# timestamp = 231412312
# bt_object = datetime.fromtimestamp(timestamp)
# print(bt_object)



# from datetime import datetime


# print(datetime.now())
# # print(datetime.timestamp(datetime.now()))


# import time

# print(time.time())



# import time
# print(time.ctime(time.time()))




# import time

# print('Print some time')
# print(time.sleep(2.4))
# print('after sleep')




# import time

# print(time.localtime(time.time()))



# import time
# print(time.gmtime(time.time()))



# from datetime import datetime

# print(datetime.now())
# print(datetime.now().strftime('%H:%M:%S'))
# print(datetime.now().time())


# import time
# print(time.localtime())
# t = time.localtime()
# print(time.strftime('%H:%M:%S', t))




from datetime import date
print(date.today())
print(date.today().strftime('%d/%m/%y'))
