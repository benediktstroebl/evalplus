
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

    output = []
    for i in s:
        # this is the #a@C
        if i.isalpha():
            # i is a@c or A@C
            if i.isupper():
                output.append(i.lower())
            # i is a@C or A@c
            else:
                output.append(i.upper())
        else:
            # i is a number
            output.append(i)

    output = ''.join(output)
    # we reverse the string
    # if it's not alphanumeric
    return output[::-1] if not output.isalnum() else output

