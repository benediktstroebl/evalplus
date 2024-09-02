
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
    lst = list(s)
    new_lst = []
    for el in lst:
        if el.isalpha():
            if el.isupper():
                new_lst.append(el.lower())
            elif el.islower():
                new_lst.append(el.upper())
        else:
            new_lst.append(el)
    return "".join(new_lst)

