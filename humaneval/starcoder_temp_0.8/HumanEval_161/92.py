
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
    if len(s) == 0:
        return s
    else:
        temp = ""
        for i in s:
            if i.isalpha():
                if i.islower():
                    temp += i.upper()
                else:
                    temp += i.lower()
            else:
                temp += i
        return temp

