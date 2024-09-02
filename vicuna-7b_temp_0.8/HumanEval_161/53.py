
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
    s_dict = {}
    for char in s:
        if char.isalpha():
            if char.lower() not in s_dict:
                s_dict[char.lower()] = char
        elif char not in s_dict:
            s_dict[char] = char
    s_reversed = ''
    for k,v in s_dict.items():
        if k.isupper():
            s_reversed += v.lower()
        else:
            s_reversed += v
    return s_reversed
