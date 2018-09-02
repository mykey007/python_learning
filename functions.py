# say hi to the user


def say_hi(name, language, animal):
    print("Hi " + name + ". You speak " + language + ". You were born in the year of the " + animal.lower() + ".")


# read top to bottom
print("***** First *****")
say_hi("Rie", "Japanese", "Rat")
print("***** Last *****")


def cube_a_number(num):
    return float(num) * float(num) * float(num)
    print("asfas") # return is the end of the function, this will never print


result = cube_a_number(4.2)

print(result)