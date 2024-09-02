
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
    length = len(string)
    if length % 2 == 0:
        length = length/2
    else:
        length = (length-1)/2

    for i in range(2,length+1):
        if string[:i] == string[i:i*2]:
            return False
    return True
