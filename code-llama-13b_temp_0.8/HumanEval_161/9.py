
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
    # Case 1 - string with no letters
    letters = [ch for ch in s if ch.isalpha()]
    if len(letters) == 0:
        return s[::-1]
    # Case 2 - string with only letters
    # Case 3 - string with letters and other characters
    else:
        new_s = ""
        for ch in s:
            if ch.isalpha():
                if ch.islower():
                    ch = ch.upper()
                else:
                    ch = ch.lower()
            new_s += ch
        return new_s
