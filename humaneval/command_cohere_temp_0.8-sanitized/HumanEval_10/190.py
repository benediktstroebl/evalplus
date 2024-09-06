def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that starts with s."""
    # Find the position of the last palindromic character
    n = len(s) - 1
    while n >= 0 and s[n] != s[n][::-1]:
        n -= 1
    if n == -1:
        return s + s[0:0]
    # Find the longest palindrome prefix of s by
    # traversing the string from the end to the start
    pre, idx = "", 0
    for i in range(n, -1, -1):
        if s[i] == s[i][::-1]:
            pre, idx = s[i:i+1], i
        else:
            break
    # Find the longest palindrome suffix of s by
    # traversing the string from the start to the end
    suf = s[::-1][-1:]
    # Create the shortest palindrome possible with the prefix and suffix
    return s[0:idx] + suf