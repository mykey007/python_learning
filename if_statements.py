# if statements

is_male = True
is_tall = False
is_alien = True

if is_male and is_tall: # use or to get the first condition

    print("Sup tall dude")

elif is_alien and not is_tall:
    print("Nanu Nanu Señor Alien")

else:
    print("Sup not-dude")


# return largest number
def max_num(num1, num2, num3):
    if num1 <= num2 and num1 != num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(0.00, -1, -34))