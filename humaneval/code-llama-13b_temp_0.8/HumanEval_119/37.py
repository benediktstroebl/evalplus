
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
    # 0 is an empty stack
    # 1 is a stack with an opening paren
    # 2 is a stack with a closing paren
    # 3 is a stack with both a closing and opening paren
    # 4 is a stack with 2 or more opening parens
    stack = 0
    for p in lst:
        if p == '(':
            if stack in (0, 1):
                stack += 1
            elif stack in (2, 3):
                stack += 2
            elif stack == 4:
                stack = 5
        elif p == ')':
            if stack in (0, 1, 2):
                stack += 2
            elif stack in (3, 4):
                stack += 1
            elif stack == 5:
                stack = 4

    if stack in (0, 1, 2):
        return 'No'
    return 'Yes'

