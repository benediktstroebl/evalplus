
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if type(string) != str:
        return False
    list_string = list(string)
    n = len(list_string)
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    return is_prime
