
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
    
    #Split the string
    str_arr = []
    for i in range(len(s)):
        str_arr.append(s[i])

    #reverse the string
    str_arr.reverse()

    #loop thru each item
    for i in range(len(str_arr)):

        #check if it is a letter or not
        if str_arr[i].isalpha():
            
            #if it is a letter, check if it is uppercase or not
            if str_arr[i].isupper():
                str_arr[i] = str_arr[i].lower()
            else:
                str_arr[i] = str_arr[i].upper()

        #else do nothing
        else:
            continue

    #join all the items and return
    return "".join(str_arr)
