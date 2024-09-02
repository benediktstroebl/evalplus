
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
    ret = ''
    for x in s:
        if x.isalpha():
            ret += x.lower() if x.isupper() else x.upper()
        else:
            ret += x
    return ret[::-1] if ret.isdigit() else ret

    # return ret[::-1] if s.isdigit() else ret
    
