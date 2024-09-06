
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
    # GoodLuck
    s_list = list(s)
    check_list = []
    for s_i in s_list:
        if not s_i.isalpha():
            s_list.remove(s_i)
        else:
            check_list.append(s_i)
    if len(check_list):
        s_list = [s_i.lower() if s_i.isupper() else s_i.upper() for s_i in s_list]
    else:
        s_list = s_list[::-1]
    return "".join(s_list)

