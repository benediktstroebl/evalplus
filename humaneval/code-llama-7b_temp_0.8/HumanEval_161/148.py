
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
    
    res = ""
    for i in s:
        if ord(i)>96 and ord(i)<123 or ord(i)>64 and ord(i)<91:
            if ord(i)>96 and ord(i)<123:
                res += chr(ord(i)-32)
            if ord(i)>64 and ord(i)<91:
                res += chr(ord(i)-32)
        else:
            res+=i
    if res=="":
        res = s[::-1]
    return res
