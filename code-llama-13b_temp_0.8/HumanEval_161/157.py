
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
    
    s1 = []
    l = len(s)
    for i in range(l):
        if s[i].islower():
            s1.append(s[i].upper())
        elif s[i].isupper():
            s1.append(s[i].lower())
        else:
            s1.append(s[i])
    if s1.isalpha():
        return s1[::-1]
    else:
        return "".join(s1)
    
    return s1
    
    
    
    
    # write your code in Python 3.6
    # 從後算前 
    # if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    # otherwise keep it as it is.
    # If the string contains no letters, reverse the string.
    # The function should return the resulted string.
    # Examples
    # solve("1234") = "4321"
    # solve("ab") = "AB"
    # solve("#a@C") = "#A@c"
    

