
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
    return s.translate(str.maketrans({'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F',
                                      'g':'G','h':'H','i':'I','j':'J','k':'K',
                                      'l':'L','m':'M','n':'N','o':'O','p':'P',
                                      'q':'Q','r':'R','s':'S','t':'T','u':'U',
                                      'v':'V','w':'W','x':'X','y':'Y','z':'Z'}))
