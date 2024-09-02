
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Write a function that takes a string and returns True if the string
    # length is a prime number or False otherwise
    # Use a list of prime numbers less than the square root of the string length
    # and a counter to check if the string length is a prime number
    # Use a recursive function to check if the string length is prime
    # or use an iterative approach

    # example 1: recursive approach
    if len(string) == 1:
        return True
    elif len(string) == 2:
        return True
    elif string[0] == '1':
        return True
    elif string[-1] == '1':
        return True
    elif len(string) % 2 != 0:
        return True
    else:
        for i in range(3, int(sqrt(len(string)) + 1) ** 2):
            if string[i:i+2] == '11':
                return True
        return False

    # example 2: iterative approach
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for num in prime_numbers:
        if len(string) % num == 0:
            return False
    return True
