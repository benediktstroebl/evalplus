
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
    s = s.lower() #convert string to lower case
    s = s.strip() #remove leading and trailing whitespaces
    s = s.translate(str.maketrans("", "", string.punctuation)) #remove punctuations
    s = ''.join([reversed(c) if c.isalpha() else c for c in s]) #reverse case
    return s