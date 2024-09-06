
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
    s = s.lower() # convert the string to lowercase
    s = s.translate(str.maketrans("", "", string.punctuation)) # remove punctuations
    s = s.translate(str.maketrans("", " ", string.ascii_letters)) # convert spaces to letters
    s = s.translate(str.maketrans("", "_", string.punctuation)) # convert punctuations to underscores
    s = s.upper() # convert the string to uppercase
    return s
