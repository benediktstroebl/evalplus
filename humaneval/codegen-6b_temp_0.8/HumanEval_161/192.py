
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
    s_lst = list(s)
    for i,letter in enumerate(s_lst):
        if letter.isalpha():
            if letter.isupper():
                s_lst[i] = letter.lower()
            else:
                s_lst[i] = letter.upper()
    if len(s_lst) == 0:
        return ''
    return ''.join(s_lst)
