#corey b. holstege
#2018-10-18
#coding problem 2.4.2

amount = 67

quarters = amount // 25
amount -= quarters * 25
dimes = amount // 10
amount -= dimes * 10
nickels = amount // 5
amount -= nickels * 5
pennies = amount

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)