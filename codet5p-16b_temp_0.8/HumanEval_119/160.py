
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

    if len(lst) < 2: return 'Yes'
    dp = [''] * len(lst)
    for i in range(len(lst)):
        if lst[i].startswith('(') and lst[i].endswith(')'):
            dp[i] = 'Yes'
        else:
            dp[i] = 'No'

        if i > 0:
            dp[i] = dp[i] or dp[i-1]

        if i + 1 < len(lst):
            dp[i] = dp[i] or dp[i+1]
    return dp[0]
