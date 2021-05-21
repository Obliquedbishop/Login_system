def suggestion(length):
    import random
    import string
    uppercase_string = string.ascii_uppercase
    lowercase_string = string.ascii_lowercase
    punctuation_string = string.punctuation
    numbers_string = string.digits
    string_list = [uppercase_string, lowercase_string, punctuation_string, numbers_string]
    case_len = length//4
    password = ""
    for index in range(0, 4):
        for i in range(0, random.randint(1, case_len)):
            digit = list(string_list[index])[random.randint(0, len(list(string_list[index]))-1)]
            password = str(password) + str(digit)

    remaining = length - len(password)
    for i in range(0, remaining):
        password = str(password) + str(random.randint(33, 126))

    password_list = list(password)
    random.shuffle(password_list)

    print("Here's a suggested password ")
    print("".join(password_list[0: length]))


def check(password):
    import random
    import string
    uppercase_count = 0
    lowercase_count = 0
    punctuation_count = 0
    numbers_count = 0
    count_list = [uppercase_count, lowercase_count, punctuation_count, numbers_count]
    uppercase_string = string.ascii_uppercase
    lowercase_string = string.ascii_lowercase
    punctuation_string = string.punctuation
    numbers_string = string.digits
    string_list = [uppercase_string, lowercase_string, punctuation_string, numbers_string]
    case_len = len(password) // 4

    for char in password:
        for index in range(0, 4):
            if char in string_list[index]:
                count_list[index] += 1

    if 0 in count_list:
        return "weak"
    else:
        return "strong"
