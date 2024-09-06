
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Iterate through the string
    for i in range(1, len(string)):
        # Check if the string has factors less than i
        for j in range(i, len(string)):
            if (string[j:j+2] == string[j-1:j+1] or string[j:j+2] == string[j-2:j+2]) or (j-i+1 > 1 and string[j:j+2] == '0'):
                # If the string has a factor, return False
                return False
        if string[i:i+2] == string[i-1:i+1] or string[i:i+2] == string[i-2:i+2]:
            # If the string has a factor, return False
            return False
    # If the string is longer than 1 and does not have any factors, return True
    return True