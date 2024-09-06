def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # Find the position of the longest palindrome suffix in s
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extract the palindrome suffix (reverse the part before i and concatenate to s)
    suffix = s[i:] + s[:i][::-1]

    # Return the shortest palindrome string starting with s by concatenating s and the suffix
    return make_palindrome(s[:i] + suffix)