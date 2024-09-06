def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome string that starts with the input string """
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix