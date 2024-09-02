
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    is_prime = True
    for i in range(2, len(string)):
        if string[i] == '1' or string[i] == '3' or string[i] == '5' or string[i] == '7' or string[i] == '9':
            is_prime = False
            break
    return is_prime
