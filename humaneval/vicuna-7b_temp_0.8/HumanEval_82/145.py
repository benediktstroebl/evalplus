
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a for loop to check if the number of digits in the string is prime
    # if it is, return True, otherwise return False
    for i in range(1, len(string)):
        if string[i:i+2] in [string[i:i+2] for string in string_list]:
            return True
    return False
