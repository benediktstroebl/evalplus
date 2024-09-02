
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
    
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 0
    upper_case = 0
    for char in s:
        if char in lower:
            lower_case += 1
        elif char in upper:
            upper_case += 1

    if upper_case and lower_case or not (upper_case or lower_case):
        return s[::-1]
    else:
        if lower_case:
            return s.swapcase()
        elif upper_case:
            return s
        
