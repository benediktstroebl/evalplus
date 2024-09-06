
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
    left = 0
    right = 0
    for p in lst[0]:
        if p == '(':
            left += 1
        elif p == ')':
            right += 1

    for p in lst[1]:
        if p == '(':
            left -= 1
        elif p == ')':
            right -= 1

    if left == 0 and right == 0:
        return 'Yes'
    return 'No'


