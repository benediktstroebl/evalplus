def make_palindrome(string):
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(''.join(filter(lambda x: x == string[0], string[::-1])))
    if i == -1:
        return string

    return string[:i] + make_palindrome(string[i+1:]) + string[i][::-1]