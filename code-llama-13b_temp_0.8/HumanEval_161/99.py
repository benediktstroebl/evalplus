
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
    ls = len(s)
    if ls == 0:
        return ""
    elif ls == 1:
        if s[0].isalpha():
            return s.swapcase()
        else:
            return s

    ls_half = int(ls / 2)
    flag = 0
    for i in range(ls_half):
        if s[i].isalpha() or s[-1 - i].isalpha():
            flag = 1
            break

    if flag == 0:
        return s[::-1]

    s1 = s[:ls_half]
    s2 = s[ls_half:]
    ret = ""
    for i, v in enumerate(s1):
        if v.isalpha():
            ret += v.swapcase()
        else:
            ret += v
    for i, v in enumerate(s2):
        if v.isalpha():
            ret += v.swapcase()
        else:
            ret += v
    return ret

