
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # base case
    if len(string) == 1:
        return True
    # middle case
    if len(string) == 2:
        return False
    # if len(string) > 2, we check if the last digit is odd or not
    if not string[-1].isdigit():
        return True
    else:
        # if the last digit is odd, the length is not a prime number
        return False
