
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
    if not s:
        return s
    if not isinstance(s,str) or not s:
        raise TypeError('solve function accepts nonempty string')
    
    letters = re.findall(r'[a-zA-Z]+',s)

    for i,l in enumerate(letters):
        if l.isupper():
            letters[i] = l.lower()
        elif l.islower():
            letters[i] = l.upper()
        else:
            letters[i] = l

    return ''.join(letters)
