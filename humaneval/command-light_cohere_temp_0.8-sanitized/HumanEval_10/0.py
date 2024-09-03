def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    palindrome = []
    for char in string:
        if char == char[::-1]:
            palindrome.append(char)

    return ''.join(palindrome)