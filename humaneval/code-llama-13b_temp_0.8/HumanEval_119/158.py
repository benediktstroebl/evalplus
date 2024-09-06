
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
    # mine
    def helper(l, r):
        if l == 0 and r == 0:
            return True
        if l == 0:
            return False
        if r == 0:
            return False
        return helper(l - 1, r - 1) or helper(l - 1, r)

    left = lst[0].count('(')
    right = lst[1].count(')')
    return 'Yes' if helper(left, right) else 'No'

