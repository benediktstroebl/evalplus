def is_palindrome(s):
    """ Test if given string is a palindrome """
    return s == s[::-1]
def make_palindrome(string):
    if is_palindrome(string):
        return string
    
    # Omit the case of a single character palindrome
    if len(string) > 1:
        for i in range(1, len(string)):
            suffix = string[-i:]
            if is_palindrome(suffix):
                prefix = string[:i][::-1]
                return string + prefix
               
    return string + string[::-1]