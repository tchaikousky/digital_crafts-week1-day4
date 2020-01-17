#1 to 10

# count = 1
# while(count <= 10):
#     print(count)
#     count += 1

#n to m

# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# flag = True

# while(flag):
#     if(start < end):
#         print(start)
#         start += 1
#     elif(start > end):
#         print(start)
#         start -= 1
#     else:
#         print(start)
#         flag = False  

#Odd Numbers

# count = 1

# while(count < 11):
#     if(count % 2 != 0):
#         print(count)
#     count += 1

#How many coins

# flag = True
# total_coins = 0

# while(flag):
#     print("You have %d coins." % total_coins)
#     user_input = input("Do you want another?").lower()
#     if(user_input == "yes"):
#         total_coins += 1
#     elif(user_input == "no"):
#         print("Bye")
#         flag = False

#Print a square

# x = 0

# while(x < 5):
#     print("*****")
#     x += 1

#Print a Square II

# x = int(input("How big is the square? "))
# y = 0

# while(y < x):
#     print("*" * x)
#     y += 1

#Print a box

# width = int(input("Width: "))
# height = int(input("Height: "))
# height_count = 0

# while(height_count < height):  
#     if(height_count == 0 or height_count == height - 1):
#         print("*" * width)
#         height_count += 1
#     else:
#         print("*" + (" " * (width - 2)) + "*")
#         height_count += 1

#Print a triangle

# count = 0
# height = 4
# current_height = 1
# width = 7

# while(count < height):
#     print(" " * int(width/2) + ("*" * current_height) + " " * int(width/2))
#     count += 1
#     current_height += 2
#     width -= 2

#Print a triangle II

# count = 0
# height = int(input("Height: "))
# current_height = 1
# width = (height - current_height)

# while(count < height):
#     print(" " * int(width) + ("*" * current_height) + " " * int(width))
#     count += 1
#     current_height += 2

#Multiplication Table
x = 1
y = 1

while(x <= 10):
    while(y <= 10):
        answer = x * y
        print("%d X %d = %d"  % (x, y, answer))
        y += 1
    print(" ")
    y = 1
    x += 1