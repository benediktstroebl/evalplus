
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the input string is empty
    if len(string) == 0:
        return False

    # Check if the input string is only one character
    if len(string) == 1:
        return True

    # Check if the input string has only digits
    digits = True
    for char in string:
        if not char.isdigit():
            digits = False
            break
    if not digits:
        return False

    # Check if the input string is a prime number
    for i in range(2, int(len(string) / 2) + 1):
        if string[i] == '0':
            continue
        if string[i] > '9':
            continue
        if string[0] % string[i] == 0:
            return False
    return True

string = input("Enter a string: ")
