
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
    
    # A flag that is set to true if there is a letter in the input string
    hasLetter = False
    
    # For each character in the string
    # if the character is a letter, reverse its case
    # if it is not a letter, leave it as it is
    # if it is a letter, set the flag to true
    # s = "".join([s[i].upper() if s[i].isalpha() else s[i] for i in range(len(s))])
    for i in range(len(s)):
        if s[i].isalpha():
            hasLetter = True
            s = s[:i] + s[i].swapcase() + s[i+1:]
    # If the flag is false, reverse the string
    if not hasLetter:
        s = s[::-1]
    return s
