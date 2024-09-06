
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Define the list of prime numbers less than or equal to the square root of the
    # length of the string
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Define the string
    string = str(string)

    # Remove leading and trailing spaces
    string = string.strip()

    # Return True if the string is in the list of prime numbers, otherwise return False
    return string in prime_list
