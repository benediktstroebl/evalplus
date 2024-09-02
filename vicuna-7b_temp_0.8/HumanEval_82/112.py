
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # loop through the string
    for i in range(1, len(string)):
        # check if the remainder is divisible by the next integer
        is_prime = True
        for j in range(2, i):
            if string[i-j] % j == 0:
                is_prime = False
                break
        if is_prime:
            return True
    return False
