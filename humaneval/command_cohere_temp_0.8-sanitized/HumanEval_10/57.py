def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:-i-1]):
        i -= 1

    # Find the longest non-palindromic prefix before the palindromic suffix
    j = 0
    while not is_palindrome(string[j:i+j+1]):
        j += 1

    # Reverse the non-palindromic prefix and concatenate
    return make_palindrome(string[:j]) + string[j:i+j+1][::-1] + make_palindrome(string[i+j+1:])