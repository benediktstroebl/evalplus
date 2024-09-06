def make_palindrome(string):
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string + string[0:]

    # Reverse the prefix before the palindromic suffix and concatenate
    return string[:i] + string[i:][::-1]