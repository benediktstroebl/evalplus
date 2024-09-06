def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # find the longest palindromic suffix
    i = len(string) - 1
    while i >= 0 and not is_palindrome(string[i:]):
        i -= 1

    # find the shortest non-palindromic prefix before the longest palindromic suffix
    j = i
    while j >= 0 and is_palindrome(string[:j+1]):
        j -= 1

    # reverse the non-palindromic prefix and append to the string
    new_string = string[i+1:] + string[:j][::-1]

    # recurse to find the shortest palindrome beginning with the new string
    return make_palindrome(new_string)