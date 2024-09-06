
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    from math import sqrt, ceil

    if len(string) <= 1:
        return False
    # same as sol 1
    if len(string) == 2:
        return True if string[0] == string[1] else False
    # Prime numbers are of the form 6k +/- 1
    # check each number up to sqrt(n)
    for x in range(2, ceil(sqrt(len(string)))):
        if string[:x] * (int(len(string) / x) + 1) == string:
            return False
    # n is prime
    return True

