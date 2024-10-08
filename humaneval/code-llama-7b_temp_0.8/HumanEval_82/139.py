
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # new_string = string.replace(" ", "")
    # length_string = len(new_string)
    # if length_string in prime_list:
    #     return True
    # else:
    #     return False

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    new_string = string.replace(" ", "")
    length_string = len(new_string)
    if length_string in primes:
        return True
    else:
        return False
