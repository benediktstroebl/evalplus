
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    s = string[0]
    for i in string[1:]:
        if is_prime(len(s)): s += i
    if is_prime(len(s)): return True
    else: return False

