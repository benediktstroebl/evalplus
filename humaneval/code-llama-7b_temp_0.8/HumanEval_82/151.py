
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    if len(string) == 2:
        return True
    if len(string) % 2 == 0:
        return False
    for num in range(3,len(string)):
        if num % 2 == 0:
            continue
        else:
            for num2 in range(3, len(string)):
                if num2 % 2 == 0:
                    continue
                else:
                    return True
    return False
