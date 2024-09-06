
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
    letters = []
    nums = []
    for letter in s:
        if letter.isalpha():
            letters.append(letter)
        else:
            nums.append(letter)
    if letters:
        for index, letter in enumerate(letters):
            if letter.isupper():
                letters[index] = letter.lower()
            else:
                letters[index] = letter.upper()
        return "".join(letters)
    else:
        return "".join(nums)[::-1]


