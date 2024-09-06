
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
    
    #isalpha checks if all chars in a string are letters
    #islower checks if all chars in a string are lowercase
    #isupper checks if all chars in a string are uppercase
    if s.isalpha():
        #if all chars in a string are letters
        if s.isupper():
            #and uppercase, return uppercase s
            return s.swapcase()
        else:
            #and lowercase, return lowercase s
            return s.lower()
    else:
        #if the string contains no letters, reverse the string
        return s[::-1]
