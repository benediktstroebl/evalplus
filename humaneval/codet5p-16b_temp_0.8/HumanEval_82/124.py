
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    len_string = len(string)
    if len_string % 2 == 0:
        return False
    else:
        return all([string[x]!= string[x+1] for x in range(0,len_string-1)])

