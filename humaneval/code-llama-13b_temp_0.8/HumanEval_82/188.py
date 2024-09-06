
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    # break the string into a list of letters
    letters = list(string)
    # remove the first letter
    letters.pop(0)
    # return the result
    return is_prime(len(string)) and is_prime(len(letters))

