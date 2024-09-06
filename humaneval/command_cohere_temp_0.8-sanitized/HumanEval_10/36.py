def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s, or an empty string if s is already a palindrome """
    if is_palindrome(s):
        return s

    # Find the longest palindromic suffix of s
    i = len(s) - 1
    while i > 0 and s[i] == s[i+1]:
        i -= 1

    # Find the longest non-palindromic prefix of s
    j = 0
    while j < len(s) // 2 and s[j] == s[len(s) - j - 1]:
        j += 1

    # Construct the palindrome by concatenating the non-palindromic prefix and the reverse of the palindromic suffix
    palindrome = s[j:i + 1] + s[j:i + 1][::-1]

    # If the constructed palindrome is empty, return s (an arbitrary choice), otherwise return the constructed palindrome
    return palindrome or s