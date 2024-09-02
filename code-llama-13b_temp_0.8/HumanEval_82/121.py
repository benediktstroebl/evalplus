
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # get the len of the string
    len_str = len(string)

    # check if it is a prime number
    for i in range(2, len_str):
        if len_str % i == 0:
            return False
    return True

