
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
    new_str = list(s)
    start, end = 0, len(new_str) - 1
    for i in range(end):
        if new_str[i].isalpha():
            while (start <= i) or (end >= i):
                if start == end:
                    break
                new_str[start], new_str[end] = new_str[end], new_str[start]
                start += 1
                end -= 1
            start = i + 1
            end = len(new_str) - 1
    return ''.join(new_str)
