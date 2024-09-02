
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
    
    # if only one letter 
    if s.count('a') + s.count('b') + s.count('c') + s.count('d') + s.count('e') + s.count('f') + s.count('g') + s.count('h') + s.count('i') + s.count('j') + s.count('k') + s.count('l') + s.count('m') + s.count('n') + s.count('o') + s.count('p') + s.count('q') + s.count('r') + s.count('s') + s.count('t') + s.count('u') + s.count('v') + s.count('w') + s.count('x') + s.count('y') + s.count('z') <= 1:
        return s[::-1]

    # if contains only letters
    if s.count('a') + s.count('b') + s.count('c') + s.count('d') + s.count('e') + s.count('f') + s.count('g') + s.count('h') + s.count('i') + s.count('j') + s.count('k') + s.count('l') + s.count('m') + s.count('n') + s.count('o') + s.count('p') + s.count('q') + s.count('r') + s.count('s') + s.count('t') + s.count('u') + s.count('v') + s.count('w') + s.count('x') + s.count('y') + s.count('z') >= 1:
        l = list(s)
        for i in range(0,len(l)):
            if l[i].islower() or l[i].isupper():
                l[i] = l[i].swapcase()

        return ''.join(l)

    # if contains letters and symbols
    if s.count('a') + s.count('b') + s.count('c') + s.count('d') + s.count('e') +
