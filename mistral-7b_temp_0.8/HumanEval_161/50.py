
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
    letters_count = 0
    if s.isalpha():
        letters_count = s.count(s)
        for i in range(len(s)):
            if s[i].isalpha():
                if s[i].islower():
                    s[i] = s[i].upper()
                else:
                    s[i] = s[i].lower()
    else:
        for i in range(len(s)):
            if s[i].isalpha():
                letters_count += 1
        if letters_count == 0:
            for i in range(len(s)):
                if not s[i].isalpha():
                    s[i] = s[i]
        else:
            s = s[::-1]

    return s
