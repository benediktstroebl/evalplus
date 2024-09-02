
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # create 2 loops, one for the items in the string, another for the remainder
    # if the remainder is 0, then its not a prime
    # other wise check the remainder for 0, return False
    # if you dont get a zero, check the string for new items
    # remove the non-letters
    # exit

    string = string.replace(' ', '').lower()
    for i in range(1, len(string)):
        if (len(string) % i == 0 and i != 1):
            return False
    return True
