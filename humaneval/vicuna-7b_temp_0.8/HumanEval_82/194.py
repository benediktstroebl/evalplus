
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check for empty string
    if not string:
        return False

    # Check if the string is a digit
    if string.isdigit():
        return False

    # Get the string length
    length = len(string)

    # Check if the string is a prime number
    for i in range(2, int(length ** 0.5) + 1):
        if string[0] == '1' and string[1] == '1':
            if string[i] == '1':
                continue
        elif string[0] != string[i]:
            continue
        elif string[0] * string[1] < string[i]:
            continue
        return True

    return False
