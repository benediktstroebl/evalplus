def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that starts with s."""
    # Find the position of the last palindromic character
    # in the string or the length of the string if none is found.
    i = len(s) - 1
    while i > 0 and s[i-1] != s[i]:
        i -= 1
    if i == 0:
        return s + s[0:1]
    else:
        # Find the longest string prefix that is a palindrome
        j = i
        while j < len(s)//2 and s[j] == s[len(s)-j-1]:
            j += 1
        return s[i:j+1] + make_palindrome(s[j+1:])