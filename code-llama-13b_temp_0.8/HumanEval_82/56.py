
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def check_prime(number):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
        return True
    
    return check_prime(len(string))
    
    
    
    # other solution
    def check_prime(number):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return False
        return True
    
    return check_prime(len(string))
