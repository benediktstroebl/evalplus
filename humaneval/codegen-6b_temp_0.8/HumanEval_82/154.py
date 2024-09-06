
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    number_of_characters = len(string)
    if number_of_characters == 1:
        return True
    elif number_of_characters == 2:
        return False
    else:
        for i in range(2, number_of_characters + 1):
            if number_of_characters % i == 0:
                return False
        return True

