def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # Find the position of the longest palindromic suffix in s
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extract the palindromic suffix (including the separator)
    palindromic_suffix = s[i:]

    # Find the separator between the palindromic suffix and the prefix
    j = i // 2
    while j < len(s) and s[i-j-1] == s[i+j]:
        j += 1

    # Extract the prefix using the separator
    prefix = s[:j]

    # Construct the new palindrome by concatenating the reversed prefix
    # and the original palindromic suffix
    new_s = palindromic_suffix + prefix[::-1]

    return new_s