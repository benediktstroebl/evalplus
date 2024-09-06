def is_palindrome(s):
    return s == s[::-1]
def make_palindrome(string):
    """Find the shortest palindrome that begins with a supplied string."""
    def palindromic_suffix(s, i=None):
        if i is None:
            i = len(s)
        if i <= 1:
            return True
        else:
            return is_palindrome(s[i-1:])

    def reverse_prefix(s, i):
        if i <= 0:
            return s
        else:
            return reverse_prefix(s[:i], i-1) + s[i:]

    # Find the longest postfix of supplied string that is a palindrome
    i = len(string)
    while True:
        if palindromic_suffix(string, i):
            break
        i -= 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + reverse_prefix(string, i-1)