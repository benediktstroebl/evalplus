def is_palindrome(string: str) -> bool:
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindrome suffix
    i = len(string) - 1
    while i >= 0 and is_palindrome(string[-i-1:]):
        i -= 1

    # Find the longest non-palindrome prefix
    j = 0
    while not is_palindrome(string[:j+1]):
        j += 1

    # Reverse the non-palindrome prefix and concatenate
    return make_palindrome(string[j:i+1]) + string[0:j] + make_palindrome(string[i+1:])