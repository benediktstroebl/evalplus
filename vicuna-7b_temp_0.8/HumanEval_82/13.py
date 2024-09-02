
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Using a list of primes up to the square root of n and checking if n is divisible by any of them
    for i in range(1, int(sqrt(string))+1):
        if string[0] == '1' and string[1:].is_prime() or string[0] == '2' and string[1:].is_prime():
            return True
        elif string[0] == '0' and string[1:].is_prime():
            return True
        elif string[0] != '1' and string[1:].is_prime():
            for j in range(2, len(string)):
                if string[j:len(string)] % i == 0:
                    return False
    return False