
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
    # 앞에서부터 검사하면서 따옴표 내부의 것만 처리하면 되는데, 파이썬에서는 별밟는다름
    # 그냥 잘 작성하면 되는데, 파이썬에서는 별밟는다름
    # 입력값 체크하고 나서 실행
    # 문제에서 입력값이 빈 문자열이라면 그냥 reverse하면 되는데, 
    # 빈 문자열에서 앞뒤 따옴표 제거하고 reverse하면 편리함
    # 파이썬에서는 별밟는다름
    if s == '':
        return s
    while s[0] == '"' or s[0] == "'":
        if s[0] == '"':
            s = s[1:]
            s = s[:len(s) - 1]
        elif s[0] == "'":
            s = s[1:]
            s = s[:len(s) - 1]
    s = s[::-1]
    return s
