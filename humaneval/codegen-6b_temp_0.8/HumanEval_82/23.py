
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # a sentence of len > 2 is palindromic if it is the same after reversing
    for i in range(2, len(string) // 2 + 1):
        if string[:i] == string[i:][::-1]:
            return True
    return False

