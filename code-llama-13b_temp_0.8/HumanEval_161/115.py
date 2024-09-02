
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
    a_z = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    other = []
    for c in s:
        if c in a_z:
            letters.append(c)
        else:
            other.append(c)
    if letters:
        letters = [l.upper() if l.islower() else l.lower() for l in letters]
        letters.extend(other)
        return ''.join(letters)
    else:
        return s[::-1]


