
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
    # obj = re.compile("[a-z]+", re.I)
    # result = obj.findall(s)
    # if len(result) == 0:
    #     return s[::-1]
    # else:
    #     return result[0].swapcase() + s.replace(result[0], "")

    # return re.sub(r"([A-Z]+|[a-z]+)", lambda x: x.group(0)[::-1], s)

    return s.swapcase() if s.isalpha() else s[::-1]

