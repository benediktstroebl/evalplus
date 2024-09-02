
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    # Your code here
    result = ""
    for i in xrange(len(s)):
        if s[i].isdigit() or (s[i].isalpha() and ord(s[i])>=97 and ord(s[i])<=122):
            result += s[i].swapcase()
        else:
            result += s[i]
    return result
