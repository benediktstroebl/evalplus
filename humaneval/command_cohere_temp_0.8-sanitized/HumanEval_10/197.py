def is_palindrome(s: str) -> bool:
    """Returns true if string s is a palindrome."""
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that starts with s."""
    if not s:
        return s

    # find the position of the longest palindrome suffix
    palindrome_idx = len(s) - len(s)[::-1] - 1

    # palindrome suffix reversed and prepended to original string
    new_s = s[:palindrome_idx] + s[::-1][palindrome_idx:][::-1]

    # if the new string is a palindrome, return it, otherwise repeat the process
    if is_palindrome(new_s):
        return new_s
    else:
        return make_palindrome(new_s)