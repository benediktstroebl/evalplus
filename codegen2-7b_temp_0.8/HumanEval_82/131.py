
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if not string:
        return False
    if string == 'a' or string == 'e' or string == 'i' or string == 'o' or string == 'u':
        return True
    if len(string) > 1:
        return all(string[0] == c for c in string[1:])
    else:
        return
