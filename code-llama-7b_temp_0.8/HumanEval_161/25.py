
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
    #print(s)
    rev = s[::-1]
    #print(rev)
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    rev_letters = letters.upper()

    rev_s = []
    for x in s:
        if x in letters:
            rev_s.append(rev_letters[letters.index(x)])
        elif x in rev_letters:
            rev_s.append(letters[rev_letters.index(x)])
        else:
            rev_s.append(x)
    rev_s = "".join(rev_s)
    
    if len(rev_s) == 0:
        return rev
    return rev_s


