
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
    
    def rev_letter(s):
        if s.isalpha():
            return s.lower() if s.isupper() else s.upper()
        return s[::-1]

    def rev_word(s):
        if s:
            return "".join(rev_letter(s[idx]) for idx in range(len(s) // 2))
        return s

    return rev_word(rev_word(rev_word(s)))

