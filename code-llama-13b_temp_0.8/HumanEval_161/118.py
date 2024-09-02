
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
    #CTCI Q 3.5
    # a = "ABCD"
    # b = "AbCd"
    # c = "#a@C"
    s_list = list(s)
    i = 0
    has_letters = False
    for item in s_list:
        if item.isalpha():
            has_letters = True
        if item.isalpha():
            s_list[i] = item.swapcase()
        i += 1
    if not has_letters:
        s_list.reverse()
    return "".join(s_list)
