def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with string s """
    if not s:
        return s

    # Find the position of the longest palindrome suffix in string s
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Find the length of the shortest prefix that forms a palindrome with suffix after i
    j = i
    while j < len(s) and not is_palindrome(s[i:j+1]):
        j += 1

    # Construct the answer as the prefix of length j followed by the reverse of the suffix after i
    return make_palindrome(s[:j]) + s[i:i+j][::-1]