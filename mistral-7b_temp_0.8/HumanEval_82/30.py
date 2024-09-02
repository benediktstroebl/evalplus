
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # convert the string to a list of characters
    string = list(string)

    # initialize the length of the string to 0
    length = 0

    # iterate over the characters in the string
    for char in string:
        # append the character to the string length
        length += 1

    # return True if the length is a prime number, otherwise return False
    return length % 2 == 1






