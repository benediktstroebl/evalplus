
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Example of using a for loop to check if a number is prime
    for i in range(2, int(string[0]) + 1):
        for j in range(2, int(string[1]) + 1):
            if string[0] == '4' or string[0] == '5' or string[0] == '6' or string[0] == '7' or string[0] == '8' or string[0] == '9':
                if (int(string[0]) - i) % j == 0 or (int(string[1]) - j) % i == 0:
                    return False
        if string[1] % j == 0:
            return False
    return True