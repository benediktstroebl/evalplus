def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome that begins with string """
    if not string:
        return string

    # Find the position of the longest palindromic suffix
    psuffix = 0
    for i in range(1, len(string)):
        if is_palindrome(string[-i:]):
            psuffix = i

    # Extract the palindromic suffix
    palind_suffix = string[-psuffix:]

    # Extract the non-palindromic prefix before the suffix
    prefix = string[:-psuffix]

    # Reverse the prefix and concatenate with the palindromic suffix
    return f"{prefix[::-1]}{palind_suffix}"