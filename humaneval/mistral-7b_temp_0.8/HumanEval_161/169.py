
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

    def is_alpha(char):
        if char.isalpha():
            return True
        else:
            return False

    if not any(is_alpha(char) for char in s):
        return s[::-1]

    temp = ""
    for char in s:
        if is_alpha(char):
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()

        temp += char

    return temp
