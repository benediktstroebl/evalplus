def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with string s """
    if not s:
        return s

    # find the longest palindrome suffix and point palindrome_end to its end
    palindrome_end = 0
    for end in range(len(s), 0, -1):
        if is_palindrome(s[::-end]):
            palindrome_end = end

    # find the closest non-palindrome prefix and remove it
    reverse_palindrome = s[::-palindrome_end]
    s = s[:-palindrome_end]

    # concatenate non-palindrome prefix and reverse palindrome
    s = s + reverse_palindrome

    return s