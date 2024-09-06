def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # algorithm idea in comment above
    if is_palindrome(string):
        return string + string
    longest_palindromic_suffix = None
    for i in range(1, len(string) + 1):
        if is_palindrome(string[-i:]):
            longest_palindromic_suffix = string[-i:]
    if longest_palindromic_suffix is None:
        return string
    return string + longest_palindromic_suffix[::-1]