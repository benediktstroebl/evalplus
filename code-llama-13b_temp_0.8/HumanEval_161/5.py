
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
    cnt = 0
    #print(s)
    for i in s:
        if(i.isalpha()):
            cnt += 1
    if(cnt == 0):
        return s[::-1]
    res = ""
    for i in s:
        if(i.isalpha()):
            if(i.isupper()):
                res += i.lower()
            else:
                res += i.upper()
        else:
            res += i
    return res


