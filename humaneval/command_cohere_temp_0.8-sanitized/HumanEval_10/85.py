def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic postfix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[i:]):
        i -= 1

    # Find the longest string prefix that comes before the palindromic suffix.
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1

    return make_palindrome(string[:j] + string[i:j][::-1] + string[j:])