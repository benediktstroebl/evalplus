
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
    def rec_helper(lst, s, memo):
        if s in memo:
            return memo[s]
        if len(lst) == 0 and s == '':
            return True

        for i in range(len(lst)):
            part = rec_helper(lst[:i]+lst[i+1:], s+lst[i], memo)
            if part == True:
                memo[s] = True
                return True
            elif part == False:
                continue

        memo[s] = False
        return False

    if len(lst) == 0:
        return 'Yes'
    if rec_helper(lst, '', {}):
        return 'Yes'
    return 'No'

