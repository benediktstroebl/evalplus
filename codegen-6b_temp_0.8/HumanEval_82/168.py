
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    flag = False
    string_length = len(string)
    for i, string_char in enumerate(string):
        if i == 0 and string_char == ' ':
            continue
        elif i == 0:
            if string_char.isdigit():
                return False
        elif i == 1 and string_char == ' ':
            continue
        elif i == 1:
            if string_char.isdigit():
                return False
        elif i == string_length - 1 and string_char == ' ':
            continue
        elif i == string_length - 1:
            if string_char.isdigit():
                return False
        elif i == string_length - 2 and string_char == ' ':
            continue
        elif i == string_length - 2:
            if string_char.isdigit():
                return False
        elif i == string_length - 2 and string_char == ' ':
            continue
        elif i == string_length - 2 and string_char.isdigit():
            return False
        for j in range(2, int(string_length / 2) + 1):
            if i % j == 0:
                return False
        if i == string_length - 1 and (j == 2 or j == int(string_length / 2)):
            flag = True
    return flag
