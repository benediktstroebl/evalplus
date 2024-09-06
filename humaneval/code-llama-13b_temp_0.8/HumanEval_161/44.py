
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
    # write your code in Python 3.6
    if not s:
        return s
    
    has_letter = False
    
    for letter in s:
        if letter.isalpha():
            has_letter = True
            break
    
    if has_letter:
        return s.swapcase()
    else:
        return s[::-1]
