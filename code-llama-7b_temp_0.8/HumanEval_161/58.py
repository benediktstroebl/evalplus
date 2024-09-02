
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
    s_reversed = list(s)
    s_reversed.reverse()
    s_reversed = ''.join(s_reversed)
    
    for idx, val in enumerate(s):
        if val.isalpha():
            if val.islower():
                s[idx] = val.upper()
            else:
                s[idx] = val.lower()
    if not s:
        return s_reversed
    else:
        return s
    
    # return s

