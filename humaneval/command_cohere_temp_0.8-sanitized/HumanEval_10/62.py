def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome that begins with string """
    if not string:
        return string

    # Find the longest palindromic suffix