
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    from collections import Counter
    cnt = Counter(string)
    for k, v in cnt.items():
        if v > 1:
            return False
    return True

