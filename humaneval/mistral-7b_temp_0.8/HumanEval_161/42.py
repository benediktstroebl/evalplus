
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
    lst = []
    for i in s:
        if i.isalpha():
            i = i.lower() if i.islower() else i.upper()
        lst.append(i)
    lst = ''.join(lst)
    return lst if ''.join(lst).isalpha() else lst[::-1]
