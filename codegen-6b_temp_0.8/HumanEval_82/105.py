
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
        return True

    for x in range(2,len(string)):
        if ((len(string) % x) == 0) and (string[(int(len(string)/x) - 1):] == string[:(len(string) % x)]):
            return False
    return True

"""
Prime Number

Write a function that takes a number and returns True if the number is a prime number,
otherwise returns False.

A number is a prime number if it only has two divisors, 1 and itself.
"""