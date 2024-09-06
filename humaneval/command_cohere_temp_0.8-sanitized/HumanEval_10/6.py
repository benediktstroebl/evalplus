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

    # Find the corresponding palindromic prefix
    j = 0
    while not is_palindrome(string[:j] + string[i:i+j][::-1]):
        j += 1

    return make_palindrome(string[:j] + string[i:i+j][::-1]) + string[i+j:]