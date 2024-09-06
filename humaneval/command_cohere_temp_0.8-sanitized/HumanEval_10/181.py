def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix of the string:
    i = len(string) - 1
    while i > 0 and is_palindrome(string[-i:]):
        i -= 1
    # Reverse the prefix up to the palindromic suffix:
    prefix = string[:i]
    return prefix + prefix[::-1]