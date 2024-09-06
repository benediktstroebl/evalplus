
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    def is_prime(num):
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    return is_prime(len(string))

    # return True if len(string) in [2,3] else False
