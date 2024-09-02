
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)
    count = 0
    if length == 2:
        return True
    for n in range(2,length+1):
        if length%n == 0:
            count += 1
    return count == 2
