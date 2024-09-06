
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
    if len(s) == 0:
        return s
    
    if s.isalnum():
        if s.islower():
            return s.swapcase()
        return s
    else:
        if s[0].isalnum():
            return s[::-1]
        else:
            i = 0
            while not s[i].isalnum():
                i += 1
                if i == len(s):
                    return s[::-1]
            if s[i].islower():
                return s[:i][::-1] + s[i:].swapcase()
            return s[:i][::-1] + s[i:]
