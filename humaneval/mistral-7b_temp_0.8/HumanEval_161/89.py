
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
    # 1
    # s1 = s.replace(s[i], s[i].upper()) if s[i].isalpha() else s[i]
    # return ''.join(s1)
    # 2
    # s1 = s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ")) if s[i].isalpha() else s[i]
    # return ''.join(s1)
    # 3
    # s1 = [s[i].upper() if s[i].isalpha() else s[i] for i in range(len(s))]
    # return ''.join(s1)
    # 4
    # return ''.join([i.upper() if i.islower() else i for i in s])
    # 5
    # if s.isalpha():
    #     return s.swapcase()
    # else:
    #     return s
    # 6
    # return s if s.is
