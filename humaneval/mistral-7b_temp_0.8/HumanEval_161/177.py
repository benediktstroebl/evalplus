
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
    ans = ""
    for letter in s:
        if letter.isalpha():
            ans += letter.upper() if letter.isupper() else letter.lower()
        else:
            ans += letter
    return ans

