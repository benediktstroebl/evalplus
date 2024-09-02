
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
    # result = ''
    # if s.isalpha()==True:
    #     if s.isupper()==True:
    #         result=s.lower()
    #     else:
    #         result=s.upper()
    # else:
    #     result=s[::-1]
    # return result
    # new_s = ''
    # for i in s:
    #     if i.isalpha():
    #         if i.islower():
    #             new_s += i.upper()
    #         else:
    #             new_s += i.lower()
    #     else:
    #         new_s += i
    # return new_s[::-1]
    return ''.join(c.lower() if c.isupper() else c.upper() for c in s[::-1] if c.isalpha())
    # return ''.join(c.lower() if c.isupper() else c.upper() for c in s[::-1] if c.isalpha())

