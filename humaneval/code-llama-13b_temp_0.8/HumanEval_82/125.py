
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # return bool(
    #     [i for i in range(2, len(string) + 1) if len(string) % i == 0] == [2])

    # check if length of string is divisible by any number between 2 and the
    # string length, excluding itself, and return True if it is only divisible
    # by 2
    return bool(
        [i for i in range(2, len(string)) if len(string) % i == 0] == [2])

