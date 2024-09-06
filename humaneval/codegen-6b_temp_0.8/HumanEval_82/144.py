
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    number = 0
    for l in string:
        number += 1
    if number == 1:
        return True
    if number == 2:
        return True
    if number == 3:
        return False
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False
    for i in range(5, int(number**0.5+1), 6):
        if number % i == 0:
            return False
    return True

