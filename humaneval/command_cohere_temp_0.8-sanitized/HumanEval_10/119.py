def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if is_palindrome(string):
        return string
    # Find the longest palindromic postfix
    i = string.rfind(string[::-1]) # [::-1] denotes reversed string
    if i == -1:
        return string
    return string.replace(string[i:i+1], '', 1)