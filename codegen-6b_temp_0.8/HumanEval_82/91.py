
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    upper_case = string.upper()
    letters = list(upper_case)
    num_of_letters = len(letters)
    for i in range(0, num_of_letters):
        if not is_prime(num_of_letters):
            return False
    return True

