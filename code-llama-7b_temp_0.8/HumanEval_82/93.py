
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if len(string) == 1 or len(string) == 0:
        return True

    if len(string) == 2:
        return False

    if len(string) == 3:
        if string[0] == string[2]:
            return True
        else:
            return False

    if len(string) % 2 == 0:
        return False

    if len(string) % 3 == 0:
        return False

    count = 1
    for i in range(0, len(string)):
        if string[i] == string[0]:
            count += 1
        if count % 2 == 0 and count % 3 == 0:
            return False
    return True
