
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # an empty string is prime
    if len(string) == 0:
        return True
    # only one character in the string is prime
    if len(string) == 1:
        return True
    # two character in the string is prime
    if len(string) == 2:
        return True
    # for all other strings, if they are prime or not depends
    # if the length is prime or not
    return len(string) in prime_list()
