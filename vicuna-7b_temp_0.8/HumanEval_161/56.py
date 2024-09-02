
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
    def count_vowels(s):
        vowels = "aeiouAEIOU"
        count = 0
        for char in s:
            if char.lower() in vowels:
                count += 1
        return count
    vowels_count = count_vowels(s)
    if vowels_count == 0:
        return s.upper()
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = s[i].upper() if vowels_count > 0 else s[i]
        if vowels_count > 0:
            vowels_count -= 1
    return s

s = input("Enter a string: ")
s = solve(s)
