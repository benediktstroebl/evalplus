
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string_len = len(string)
    
    # primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    primes_list = [num for num in range(1, 30) if num % 2 != 0 or num % 5 != 0]
    
    for prime in primes_list:
        if string_len == prime:
            return True
    return False
