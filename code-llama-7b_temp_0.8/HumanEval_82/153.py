
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Variables
    counter = 0
    # Checking if the length is a prime number
    if (len(string) == 2) or (len(string) == 3):
        return True
    elif (len(string) % 2 == 0) or (len(string) % 3 == 0):
        return False
    else:
        for num in range(2, len(string)):
            if len(string) % num == 0:
                counter += 1
        if counter == 0:
            return True
        else:
            return False
