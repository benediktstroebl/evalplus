
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    import math
    number = len(string)
    lst_prime = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            lst_prime.append(i)
    if len(lst_prime) == 0:
        return True
    else:
        return False

