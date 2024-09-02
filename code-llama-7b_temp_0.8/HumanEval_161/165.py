
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
    lower_alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    upper_alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    a_str = [i for i in s]
    for i in range(len(s)):
        if a_str[i] in lower_alphabet:
            a_str[i] = a_str[i].upper()
        elif a_str[i] in upper_alphabet:
            a_str[i] = a_str[i].lower()
    a_str = "".join(a_str)
    return a_str


