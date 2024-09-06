
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
    rev_case = []
    i = 0
    while i < len(s):
        if s[i].isalpha():
            if s[i].islower():
                rev_case.append(s[i].upper())
            else:
                rev_case.append(s[i].lower())
        else:
            rev_case.append(s[i])
        i += 1
    result = "".join(rev_case)
    return result

test = [["1234", "#a@C"], ["123", "hello", "world"], ["ab"]]
for t in test:
    print(solve(t[0]))