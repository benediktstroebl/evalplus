def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = len(string) - 1
    while i >= 0 and not is_palindrome(string[i:]):
        i -= 1

    # Find the corresponding palindromic prefix
    j = 0
    while not is_palindrome(string[:j] + string[i:i+j]):
        j += 1

    # Extract the palindromic suffix and reverse it to create the shortest palindrome
    suffix = string[i:i+j]
    reversed_suffix = suffix[::-1]
    return string[:j] + reversed_suffix