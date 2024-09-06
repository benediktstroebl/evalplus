
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string is empty
    if len(string) == 0:
        return True
    
    # Check if the string is only one character
    if len(string) == 1:
        return False
    
    # Use a for loop to check if the string is prime
    for i in range(2, len(string)):
        if string[0] == string[i]:
            return False
        elif string[i:len(string)] in ['0','1','2','3','4','5','6','7','8','9']:
            return False
    
    # If the string is not divisible by any number between 2 and its length, it is a prime number
    return True
