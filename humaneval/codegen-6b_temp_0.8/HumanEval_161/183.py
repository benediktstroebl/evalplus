
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
    elif len(s) == 1:
        return s
    else:
        curr_char = s[0]
        if curr_char.isalpha():
            curr_char = curr_char[::-1]
            if curr_char is not None:
                curr_char = curr_char.lower()
                return curr_char + solve(s[1:])
            else:
                return solve(s[1:])
        else:
            curr_char = curr_char[::-1]
            return curr_char + solve(s[1:])
