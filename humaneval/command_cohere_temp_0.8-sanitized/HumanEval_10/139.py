def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # find the position of the longest palindromic suffix
    max_len, palindromic_suffix_pos = 0, 0
    for i in range(1, len(s)):
        if is_palindrome(s[i:]):
            palindromic_suffix_pos = i
            max_len = max(max_len, i)

    # reverse the non-palindromic prefix and append to the palindromic suffix
    return make_palindrome(s[:palindromic_suffix_pos] + s[-(i+1):] + s[palindromic_suffix_pos:-(i+1)])