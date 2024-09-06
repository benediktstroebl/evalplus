def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix of the string
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1

    # Find the longest non-palindromic prefix of the string
    j = 0
    while j < len(string) // 2 and is_palindrome(string[j:j+len(string) // 2]):
        j += 1

    # Construct the shortest palindrome
    return make_palindrome(string[j:i] + string[::i-j-1] + string[-i:j-1])