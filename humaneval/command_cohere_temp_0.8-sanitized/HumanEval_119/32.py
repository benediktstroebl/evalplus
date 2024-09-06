def match_parens(lst):
    if len(lst) != 2:
        return "Invalid input"
    s = ['(', ')', '*', '+', '^']
    dp = [0] * (1 << len(s))
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] + s[j] in lst:
                dp[i | j] = 1
    if sum(dp) == 0:
        return "No"
    return "Yes"