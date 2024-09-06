
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
    list_s = list(s)
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if s.isalpha() == False:
        i = 0
        while i < len(list_s):
            if list_s[i] in letters:
                if list_s[i].islower():
                    list_s[i] = list_s[i].upper()
                else:
                    list_s[i] = list_s[i].lower()
                i += 1
            else:
                i += 1
        return "".join(list_s)

    else:
        i = 0
        while i < len(list_s):
            if list_s[i] in letters:
                if list_s[i].islower():
                    list_s[i] = list_s[i].upper()
                else:
                    list_s[i] = list_s[i].lower()
                i += 1
            else:
                i += 1
        return "".join(list_s)
    # for i in range(len(s)):
    #     if s[i] in letters:
    #         if s[i].islower():
    #             s[i] = s[i].upper()
    #         else:
    #             s[i] = s[i].lower()
    # return s
