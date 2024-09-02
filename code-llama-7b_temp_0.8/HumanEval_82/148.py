
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # 1. Length of the string
    string_length = len(string)
    # 2. Length of the string is a prime number or not
    # This is a check for a number divisible by 2 but not by 3
    if string_length % 2 == 0 and string_length % 3 != 0:
        # 3. Return True
        return True
    # 4. Length of the string is not a prime number or not
    else:
        # 5. Return False
        return False

