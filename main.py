# check if number is divisible by 3, 5, or both. Returns string
def dev_check(number):
    if number % 3 == 0 and number % 5 == 0:
        return " -- Both"
    elif number % 5 == 0:
        return " -- 5"
    elif number % 3 == 0:
        return " -- 3"
    else:
        return ""


# request user input
starting_value = int(input("Please enter starting value: "))
ending_value = int(input("Please enter ending value: "))

# loop through user specified range
for i in range(starting_value, ending_value + 1):
    print(str(i) + dev_check(i))

