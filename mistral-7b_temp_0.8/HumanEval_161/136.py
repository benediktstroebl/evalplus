
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
    # remove punctuation and numbers
    result = "".join(filter(lambda x: x.isalpha(), s))

    # if no letters in the string
    if len(result) == 0:
        result = s[::-1]
        return result

    # convert letters to lower case
    for i in range(len(result)):
        result[i] = result[i].lower()

    return result


