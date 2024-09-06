
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
    
    def reverse_letter(text):
        rev_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    rev_text += text[i].lower()
                else:
                    rev_text += text[i].upper()
            else:
                rev_text += text[i]
        return rev_text
    rev_s = reverse_letter(s)
    rev_s = rev_s[::-1]
    return rev_s
    
