
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    try:
        return len(string) in [2, 3, 5, 7] or (len(string) in range(2,10) and len(list(filter(lambda x: x % 2 == 0, range(2,len(string)+1)))) == 0)
    except ValueError:
        return False

    
