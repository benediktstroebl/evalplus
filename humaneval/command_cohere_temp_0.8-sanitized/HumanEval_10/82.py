def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix in the string
    i = len(string) - 1
    while i >= 0 and not is_palindrome(string[-i-1:]):
        i -= 1

    # If no palindromic suffix, return the original string
    if i == -1:
        return string

    # Reverse the string from the start to the palindromic suffix, and append the reverse of the prefix before the suffix
    return make_palindrome(string[:i] + string[i:i+1][::-1] + string[i+1:])