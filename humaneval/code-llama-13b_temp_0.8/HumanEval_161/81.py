
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
    
    # your code goes here
    letter_flag = False
    res = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                res += char.lower()
            else:
                res += char.upper()
            letter_flag = True
        else:
            res += char
            
    if letter_flag is False:
        res = res[::-1]
    return res
