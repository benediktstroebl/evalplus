
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
    letters = []
    for i in range(len(s)):
        if s[i].isalpha():
            letters.append(s[i])
    
    
    reversed_letters = []
    for l in letters:
        if l.isupper():
            reversed_letters.append(l.lower())
        else:
            reversed_letters.append(l.upper())
    
    return "".join(reversed_letters)


assert solve("ab") == "AB"
assert solve("1234") == "4321"
assert solve("#a@C") == "#A@c"
assert solve("d") == "d"
assert solve("") == ""
assert solve("#$%") == "#$%
assert solve("#  $%") == "#  $%
assert solve("#abc") == "#Abc"
assert solve("1234") == "4321"
