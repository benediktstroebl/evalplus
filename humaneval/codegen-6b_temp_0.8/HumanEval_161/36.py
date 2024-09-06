
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
    result = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                result = result + c.upper()
            else:
                result = result + c.lower()
        else:
            result = result + c
    return result

assert solve("ab") == "AB"
assert solve("#a@C") == "#A@c"
assert solve("1234") == "4321"
assert solve("cccccccc") == "cccccccc"
assert solve("") == ""
assert solve("a") == "A"
assert solve("#a@$") == "#A@$"
assert solve("A") == "A"
assert solve("#a@$") == "#a@$"
assert solve("a#") == "a#"
assert solve("#a@$") == "#a@$"
assert solve("a$") == "a$"
assert solve("$") == "$"
assert solve("AB") == "AB"
assert solve("AA") == "AA"
assert solve("Aa") == "Aa"
assert solve("abb") == "bbb"
assert solve("a#") == "bbb"
assert solve("a#bbb") == "a#bbb"
assert solve("bba") == "aba"
assert solve("bbb") == "bbb"
assert solve("") == ""
assert solve("#") == ""
assert solve("#a@$") == "#a@$"
assert solve("") == ""
assert solve("") == ""
assert solve("") == ""
assert solve("") == ""
assert solve("") == ""
assert solve("") == ""
assert solve("") == ""
