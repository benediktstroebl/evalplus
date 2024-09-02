
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # s = string
    # c = 0
    # for i in range(1, len(s)+1):
    #     if len(s)%i == 0:
    #         c +=1
    # if c > 2:
    #     return False
    # else:
    #     return True
    # return True if len(string)%2 != 0 else False
    return True if len(string)%2 != 0 else False


