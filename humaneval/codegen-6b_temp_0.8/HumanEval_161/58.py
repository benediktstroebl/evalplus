
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
    if not s:
        return s
    
    u = []
    l = 0
    for e in s:
        if e.isalpha():
            e = e.lower() if e.islower() else e.upper()
            u.append(e)
            l += 1
    
    return ''.join(u[::-1]) if l == 0 else ''.join(u)

