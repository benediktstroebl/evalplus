
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(number):
        if number < 2:
            return False
        if number in [2, 3, 5, 7]:
            return True
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            return False
        return True
    return is_prime(len(string))

