
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
    # using stack to keep the state of each char
    result = []
    st = [False] * 26
    for char in s:
        if char.isupper():
            st[ord(char) - ord('A')] = True
        elif char.islower():
            st[ord(char) - ord('a')] = True
        elif char.isalpha():
            result.append(char)
    if not any(st):
        result.append('')
    else:
        result = [st[idx] for idx in result if not st[idx]]
        if any(c.isupper() for c in result[::-1]):
            result = [''.join(reversed(c)) for c in result if c]
    return ''.join(result)
