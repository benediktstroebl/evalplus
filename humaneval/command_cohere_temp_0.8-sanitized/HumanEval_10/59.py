def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    # Find the longest palindrome suffix in the string
    i = len(s) - 1
    while i >= 0 and not is_palindrome(s[i:]):
        i -= 1
    # If no palindrome suffix, return s
    if i == -1:
        return s
    # Otherwise extend the palindrome backward
    j = i - 1
    while j >= 0 and s[j] == s[i]:
        j -= 1
    sj = s[j:i+1]
    # Find the shortest prefix that matches with the reverse of the palindrome suffix
    k = 0
    while k < len(sj) and sj[k] == sj[::-1][k]:
        k += 1
    # Extend the palindrome forward if possible, otherwise just return the palindrome suffix
    if k < len(sj):
        return sj + s[k:i+1][::-1]
    else:
        return sj