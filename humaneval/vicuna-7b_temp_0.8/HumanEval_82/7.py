
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    if len(string) > 1:
        for i in range(2, int(len(string) / 2) + 1):
            if string[i:i+2] in string:
                return False
        return True
    else:
        return False
