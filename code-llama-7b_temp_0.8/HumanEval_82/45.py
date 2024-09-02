
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    #create a variable that stores the length of the string
    length = len(string)
    #create a variable that stores a boolean value of whether the length is prime
    is_prime = False
    #create a for loop that checks if length is prime
    for i in range(2, length):
        if length % i == 0:
            is_prime = True
            break
        else:
            is_prime = False
    return is_prime
