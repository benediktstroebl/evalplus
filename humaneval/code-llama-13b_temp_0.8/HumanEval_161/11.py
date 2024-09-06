
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
    s_list = list(s)
    # s_list = [char for char in s]
    l_c = 0
    u_c = 0
    for i in s_list:
        if i.isalpha():
            if i.islower():
                l_c += 1
            elif i.isupper():
                u_c += 1
    if l_c > u_c:
        s_list = [i.upper() if i.isalpha() else i for i in s_list]
    elif u_c > l_c:
        s_list = [i.lower() if i.isalpha() else i for i in s_list]
    else:
        s_list = s_list[::-1]
    return "".join(s_list)

