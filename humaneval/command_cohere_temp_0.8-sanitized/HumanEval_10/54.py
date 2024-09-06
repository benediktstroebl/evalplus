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

    # Extract the palindromic suffix (reverse the part before i and concatenate to s)
    palindromic_suffix = s[i:] + s[:i][::-1]
    s = s[:i]

    # If the palindromic suffix is empty, return s (no need to modify)
    if len(palindromic_suffix) == 0:
        return s

    # Otherwise, continue to find the shortest palindrome
    while i < len(s):
        # Find the prefix before the palindromic suffix
        j = 0
        while not is_palindrome(s[i-len(palindromic_suffix) + j: i-len(palindromic_suffix)]):
            j += 1

        # Extract the reverse of the prefix and concatenate to s
        s = s[:i-len(palindromic_suffix) + j] + palindromic_suffix[::-1] + s[i-len(palindromic_suffix) + j:]

        # Move i to the position after the newly concatenated palindromic suffix
        i += len(palindromic_suffix) - j

    return s