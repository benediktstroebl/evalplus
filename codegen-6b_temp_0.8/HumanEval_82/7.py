
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def _prime_check(string):
        """check if a string is a prime number"""
        if (string == ''.join(set(string)) and len(string) == 1):
            return True
        else:
            return False
    def _string_length(string):
        """return the length of a string"""
        return len(string)
    def _half_length(string):
        """return the length of the half of a string"""
        return len(string) // 2
    # check if the string length is a prime number
    if _string_length(string) % 2 == 0:
        return True
    else:
        # if not check if the half of the string length is a prime number
        if _prime_check(string[:_half_length(string)]) == True:
            # check if the half of the string length is a prime number
            if _prime_check(string[_half_length(string):]) == True:
                return True
            else:
                return False
        else:
            return False
