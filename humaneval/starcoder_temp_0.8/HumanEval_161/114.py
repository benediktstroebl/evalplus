
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
    # your code here
    s=s.lower()
    i=0
    while(i<len(s)):
        if s[i].isalpha():
            s=s[0:i]+s[i].swapcase()+s[i+1:len(s)]
        i+=1
    return s
