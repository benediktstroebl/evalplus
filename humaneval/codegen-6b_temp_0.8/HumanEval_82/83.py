
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    n = 0
    for i in string:
        n += 1
    if n > 1:
        return all(n % i for i in range(2, n))
    else:
        return n == 1

