def make_palindrome(string):
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string+string[::-1]

    return string[:i+1]+string[i+1:i][::-1]