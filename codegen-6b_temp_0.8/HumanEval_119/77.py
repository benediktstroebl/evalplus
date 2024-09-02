
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
    # we need to do a stack for each layer
    stk1, stk2 = [], []

    for s in lst:
        if s == ')' and len(stk1) == 0:
            return 'No'
        if s == '(':
            stk1.append('(')
        if s == ')':
            if len(stk1) == 0:
                return 'No'
            stk2.append(')')
            stk1.pop()

    return 'Yes' if len(stk1) == len(stk2) else 'No'


