
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
    left = []
    for i in lst[0]:
        if i == '(':
            left += [i]
        elif i == ')':
            try:
                left.pop()
            except IndexError:
                return 'No'
    if left:
        return 'No'
    
    right = []
    for i in lst[1]:
        if i == ')':
            right += [i]
        elif i == '(':
            try:
                right.pop()
            except IndexError:
                return 'No'
    if right:
        return 'No'
    return 'Yes'
