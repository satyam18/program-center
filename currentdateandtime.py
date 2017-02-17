Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def current_date_and_time(date,time):
	"""(int,int) -> int
        returns the current date and time
        """

	
>>> import datetime
>>> now = datetime.datetime.now()
>>> print ("Current date and time : ")
Current date and time : 
>>> print (now.strftime("%Y-%m-%d %H:%M:%S"))
2017-02-17 19:00:46
>>> 
