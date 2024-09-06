
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    counter = 0
    length = len(string)
    for i in range(1,length+1):
        if length % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False
    
