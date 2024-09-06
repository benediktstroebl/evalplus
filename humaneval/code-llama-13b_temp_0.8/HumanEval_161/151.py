
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
    no_letters = []
    res = []
    for i in s:
        if i.isalpha():
            letters.append(i)
        else:
            no_letters.append(i)

    if len(letters) > 0:
        res = [chr(ord(i) ^ 32) if i.islower() else i for i in letters]
    else:
        res = [i for i in no_letters]
        res = res[::-1]

    return "".join(res)

