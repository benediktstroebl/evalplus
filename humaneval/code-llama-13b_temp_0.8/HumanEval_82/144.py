
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def prime_checker(number):
        if number <= 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    return prime_checker(len(string))
