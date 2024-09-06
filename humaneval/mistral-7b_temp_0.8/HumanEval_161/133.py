
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
    # your code here
    string_to_list = list(s)
    for i in range(len(string_to_list)):
        if string_to_list[i].isalpha():
            if string_to_list[i].islower():
                string_to_list[i] = string_to_list[i].upper()
            else:
                string_to_list[i] = string_to_list[i].lower()
        elif string_to_list[i].isdigit():
            pass
    string_to_list = ''.join(string_to_list)
    return string_to_list

