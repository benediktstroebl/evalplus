
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
    if not lst:
        return 'Yes'
    if len(lst) == 1:
        if lst[0] == ')':
            return 'No'
        else:
            return 'Yes'
    stack_left = []
    stack_right = []
    for i in lst:
        if i == '(':
            stack_left.append(')')
        elif i == ')':
            if stack_left:
                stack_left.pop()
            else:
                stack_right.append(')')
    if not stack_left and not stack_right:
        return 'Yes'
    return 'No'
