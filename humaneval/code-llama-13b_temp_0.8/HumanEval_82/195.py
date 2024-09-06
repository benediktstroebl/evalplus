
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # def isPrime(number):
    #     if number == 1:
    #         return False
    #     for x in range(2,number):
    #         if number%x == 0:
    #             return False
    #     return True

    # for n in range(2, len(string)):
    #     if len(string)%n == 0:
    #         return False
    # return True

    if len(string) < 2:
        return False
    for i in range(2, len(string)):
        if len(string)%i == 0:
            return False
    return True
