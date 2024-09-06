def make_palindrome(string):
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(''.join(filter(lambda x: x == string[0], string[::-1])))
    if i == -1:
        return string

    # Reverse the prefix before the palindromic suffix and append it
    return make_palindrome(string[:i]) + string[i:i+1][::-1]