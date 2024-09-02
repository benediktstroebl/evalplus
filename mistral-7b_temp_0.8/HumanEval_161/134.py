
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


    # 짠 코드
    # return s.translate(str.maketrans({" ": " "} | str.upper(), str.lower(), str.lower(), str.upper()))

    # 풀이 참조
    # return s.translate({ord(s[i]): ord(s[i].swapcase()) for i in range(len(s))})
    return s.translate({ord(s[i]): ord(s[i].swapcase()) for i in range(len(s))})

