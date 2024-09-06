
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
    a = list(s)
    for i in range(len(a)):
        if a[i].isalpha():
            if a[i].islower():
                a[i] = a[i].upper()
            elif a[i].isupper():
                a[i] = a[i].lower()
            else:
                print("?")
    return "".join(a)
