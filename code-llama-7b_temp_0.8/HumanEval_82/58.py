
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime = True
    string_length = len(string)
    for number in range(2,string_length):
        if string_length%number==0:
            prime = False
    return prime
    
