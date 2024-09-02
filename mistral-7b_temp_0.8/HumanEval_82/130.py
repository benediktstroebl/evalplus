
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_number = True
    for number in range(2,len(string)):
        if len(string) % number == 0:
            prime_number = False
            break
    if prime_number == True:
        return True
    else:
        return False

