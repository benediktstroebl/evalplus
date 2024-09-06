def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1

    # Reverse the prefix up to the palindromic suffix
    reversed_prefix = string[:i][::-1]
    return f"{reversed_prefix}{string[i:]}"