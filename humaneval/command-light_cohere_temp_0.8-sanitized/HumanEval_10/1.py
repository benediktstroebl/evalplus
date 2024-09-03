def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string: return ''
    l = len(string)
    while l:
        p = string[l-1:l]
        if p == p[::-1]:
            return string[:l-1] + p[::-1]
        l -= 1
    return ''