
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
    result = ''
    n = len(s)
    for i in range(n):
        # print('i', s[i])
        # print('s[i-1]', s[i-1])
        # print('s[i+1]', s[i+1])
        # print('i from 0 to n-1', i)
        c = s[i]
        print('c', c)
        if c.isalpha():
            if c.isupper():
                result += c.lower()
            elif c.islower():
                result += c.upper()
        else:
            result += c
    print('result', result)
    return result

