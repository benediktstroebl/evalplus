def match_parens(s):
    '''
    Check if it is possible to concatenate two strings consisting of open
    and close parentheses, such that the resulting string is balanced.
    '''
    if ")" not in s[0] or "(" not in s[1]:
        return "No"
    if ")" in s[0] and "(" in s[1]:
        return "No"
    s1 = s[0].replace("(", ""). replace(")", "")