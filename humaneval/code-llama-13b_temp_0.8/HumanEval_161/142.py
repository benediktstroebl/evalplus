
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
    # return string
    new_str = []
    is_alpha = False
    for ch in s:
        if ch.isalpha():
            is_alpha = True
        if ch.isalpha():
            if ch.isupper():
                new_str.append(ch.lower())
            else:
                new_str.append(ch.upper())
        else:
            new_str.append(ch)
    if is_alpha:
        return ''.join(new_str)
    return ''.join(reversed(new_str))
    
    
