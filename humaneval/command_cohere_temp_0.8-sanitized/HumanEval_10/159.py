def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix.
    i = len(string) - 1
    while i >= 0 and is_palindrome(string[-i-1:]):
        i -= 1
    # Find the corresponding palindromic prefix.
    j = 0
    while j < i and is_palindrome(string[j:i]):
        j += 1
    # Return the shortest palindrome by trimming the ends if they differ.
    return string[:j] if len(string) == i + j + 1 else string[j:i+j+1][::-1].replace('', 'a')