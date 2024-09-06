def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix of the string:
    i = len(string) - 1
    while i >= 0 and is_palindrome(string[-i-1:]):
        i -= 1
    # Reverse the string up to the palindromic suffix to get the shortest palindrome:
    return string[:i] + string[i:][::-1]