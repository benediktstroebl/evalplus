
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    prime = 2
    string = len(string)
    while prime < string:
        if string % prime != 0:
            prime += 1
        else:
            return False
    return True

