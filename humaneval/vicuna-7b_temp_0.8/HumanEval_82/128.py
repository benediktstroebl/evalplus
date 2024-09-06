
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Find prime numbers less than or equal to the square root of the
    # length of the string
    for i in range(int(np.sqrt(len(string)) + 1)):
        if string[i] == '1':
            for j in range(i + 1, len(string)):
                if string[j] == '1':
                    return False
                if (string[j] - i) % string[i] != 0:
                    return False
    return True
