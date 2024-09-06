
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
    def count_letters(s):
        count = 0
        for char in s:
            if char.isalpha():
                count += 1
        return count
    count = count_letters(s)
    if count == 0:
        return s.upper()
    else:
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = s[i].upper() if s[i].isupper() else s[i].lower()
        return s

s = input()
result = solve(s)
