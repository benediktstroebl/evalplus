def make_palindrome(string: str, join_char: str = 'c') -> str:
    """ Returns the shortest palindrome string that begins with string """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string + join_char + make_palindrome(string, join_char)

    # Go backward to the maximum length palindrome beginning at s[0]
    for j in range(i, 0, -1):
        if string[j] != string[j-1]:
            break
        i = j

    return make_palindrome(string[:i] + join_char + string[i:][::-1], join_char)