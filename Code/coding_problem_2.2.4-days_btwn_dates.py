# corey b. holstege
#	2018-09-19

from datetime import date
import random
earlier_date = date(2017, 6, random.randint(1, 25))
later_date = date(2017, 6, random.randint(earlier_date.day + 1, 28))


#Here, all we need to do is subtract the day number of the earlier
#date from the day number of the later date.
days_between = later_date.day - earlier_date.day


print("There are", days_between, "days between", earlier_date, "and", later_date)