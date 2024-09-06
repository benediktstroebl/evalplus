
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
    # a = s.lower()
    # b = s.upper()
    # if len(a) == 0:
    #     return s
    # else:
    #     for i in range(len(a)):
    #         if a[i].isalpha():
    #             # if the previous char is uppercase, the current char should be lowercase
    #             a[i] = a[i].isupper() and a[i-1].islower() or a[i].islower() and a[i-1].isupper()
    #         else:
    #             a[i] = a[i]
    #     return ''.join(a)
    # print(solve("1234"))
    # print(solve("ab"))
    # print(solve("aBcD"))
    # print(solve("a@c"))
    # print(solve("123456789"))
    # print(solve("!@#$%^&*"))
    # print(solve("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
    
    return s
