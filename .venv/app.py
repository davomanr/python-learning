# # v = "Hello World"
# # x=30
# #
# # if x>100:
# #  print (x)
# # elif x > 2000:
# #   print(v)
# # else:
# #   print(v)
# # #Ask the user for their weight
# # weight=float (input("weight: "))
# #
# # #Ask user to input unit type
# # unit = input("(K)g or (L)bs: ")
# #
# # #Check which unit was entered
# # if unit == "L" or "l":
# #   converted = weight * 0.453592  # pounds to kilograms
# #   print("Weight in Kg:", round(converted, 2))
# # elif unit == "K" or k:
# #     converted = weight / 0.453592  # kilograms to pounds
# #     print("Weight in Lbs:", round(converted, 2))
# # else:
# #     print("Invalid unit. Please enter K or L.")
#
# # i=int (input("Enter a number: "))
# # while i>=0:
# #     print(i * 'Hi ')
# #     #i=int (input("Enter a number: "))
# #     i-=1
#
# # names = ['John', 'Sam', 'Lee']
# # names.insert (1, 'dee')
# # if ("Jake" in names):
# #     print('Jake is in the list')
# # elif ('Sm' in names):
# #     print('Sam is in the list')
# # else:
# #     print(len(names))
#
# # names = ['John', 'Sam', 'Lee']
# # for x in names:
# #   print(x + ' is a ' + x)
# #
# # while  len(names) >0:
# #   print(names.pop())
#
# x = 0  # counter for even numbers
#
# for i in range(1, 11):  # goes from 1 to 10
#     if i % 2 == 0:      # check if even
#         x += 1
#
# print('The number of even numbers is ' + str(x))

# def dataread(first_name , last_name):
#
#     print(f'Hi {first_name + " " + last_name} Welcome to the world of Python!')
#
# dataread("dani","manr")

# def greatings (name):
#     return (f"Hello {name}, welcome to the world of Python!")
# message = greatings("JK")
# print(message)

def argument(*numbers):
    x=0
    for number in numbers:
        x=x+ number
    print(x)
argument(1, 2, 3, 4)


