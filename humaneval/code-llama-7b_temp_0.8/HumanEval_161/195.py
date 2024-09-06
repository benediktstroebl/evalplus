
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
    list1 = list(s)
    for i in range(len(list1)):
        if list1[i].isalpha():
            if list1[i].islower():
                list1[i] = list1[i].upper()
            elif list1[i].isupper():
                list1[i] = list1[i].lower()
            else:
                list1[i] = list1[i]
        elif list1[i].isnumeric():
            if list1[i].isdigit():
                list1[i] = str(int(list1[i])*-1)
            else:
                list1[i] = list1[i]
        else:
            if list1[i].isdigit():
                list1[i] = str(int(list1[i])*-1)
            else:
                list1[i] = list1[i]
    return "".join(list1)
    #return "".join([x.lower() if x.isupper() else x.upper() if x.islower() else x for x in s])

