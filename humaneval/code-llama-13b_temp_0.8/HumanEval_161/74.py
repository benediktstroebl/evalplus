
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
    # Write your code here
    count = 0
    if len(s) == 0:
        return s
    for i in range(len(s)):
        if s[i].isalpha():
            count += 1
    if count == 0:
        return s[::-1]
    else:
        new_s = ""
        for i in range(len(s)):
            if s[i].isalpha():
                if s[i].isupper():
                    new_s += s[i].lower()
                else:
                    new_s += s[i].upper()
            else:
                new_s += s[i]
        return new_s

