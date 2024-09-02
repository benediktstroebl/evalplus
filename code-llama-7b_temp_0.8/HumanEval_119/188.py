
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''

    # DFS + stack
    # dp table: dp[i][j] = is_good(i, j)
    # dp[i][j] = dp[i][j-1] and dp[i-1][j]
    # dp[i][j] = false if dp[i-1][j] is false
    # dp[i][j] = true if dp[i][j-1] is true
    # dp[i][j] = dp[i-1][j-1] if dp[i-1][j] is true and dp[i][j-1] is true
    # or dp[i-1][j-1] if dp[i-1][j] is true and dp[i][j-1] is false
    # O(n*m) time and space, n is the length of the first string, m is the length of the second string
    # Exceeded time limit.
    # n, m = len(lst[0]), len(lst[1])
    # dp = [[False] * (m+1) for _ in range(n+1)]
    # dp[0][0] = True
    # for i in range(1, n+1):
    #     for j in range(1, m+1):
    #         dp[i][j] = dp[i][j-1] and dp[i-1][j]
    #         if not dp[i-1][j]:
    #             dp[i][j] = False
    #         if not dp[i][j-1]:
    #             dp[i][j] = False
    #         if dp[i-1][j] and dp[i][j-1]:
    #             dp[i][j] = True
    #         if dp[i-1][j] and not dp[i][j-1]:
    #             dp[i][j] = dp[i-1][j-1]
    # if dp[n][m]:
    #     return 'Yes'
    # return '
