
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def check_prime(num):
        if num == 1 or num == 2:
            return True
        elif num < 1:
            return False
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
                else:
                    continue
            return True
    return check_prime(len(string))
