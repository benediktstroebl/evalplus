
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
    result = []
    
    if s.isdigit():
        result = s[::-1]
    else:
        for i in s:
            if i.isdigit():
                result.append(i)
            else:
                if i.islower():
                    result.append(i.upper())
                else:
                    result.append(i.lower())
    
    if s.isdigit() or not s.isalpha():
        return "".join(result[::-1])
    else:
        return "".join(result)
