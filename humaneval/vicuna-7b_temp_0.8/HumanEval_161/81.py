
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
        return "".join(sorted(s))
    for i in range(len(s)):
        if s[i].isalpha():
            s = s.replace(s[i], s[i].upper() if s[i].islower() else s[i].lower())
        else:
            s = s.replace(s[i], s[i])
    return s

test = [("1234", "4321"), ("ab", "AB"), ("a@c", "#A@c"), ("", "")]
solutions = []
for case in test:
    solution = solve(case[0])
    if solution != case[1]:
        print(f"Error: expected '{case[1]}' but got '{solution}'")
    else:
        solutions.append(solution)
