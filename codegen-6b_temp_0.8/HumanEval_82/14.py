
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) < 3:
        return True
    if len(string) % 2 == 0:
        return False
    return all(string[i] == string[len(string)-i-1] for i in range(len(string)//2))
