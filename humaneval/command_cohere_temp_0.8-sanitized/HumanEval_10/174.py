def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = len(string) - 1
    while i > 0 and string[i] == string[i - 1]:
        i -= 1

    # Find the longest non-palindromic prefix before the palindromic suffix
    j = 0
    while string[j] == string[i]:
        j += 1

    # Reverse the non-palindromic prefix and concatenate
    return make_palindrome(string[j:i] + string[i:j][::-1]) + string[j:]