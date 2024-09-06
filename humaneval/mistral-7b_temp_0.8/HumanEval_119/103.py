
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
    if len(lst) == 0:
        return 'Yes'
    if len(lst) == 1:
        return lst[0][0] == '(' and lst[0][-1] == ')'

    for i in range(len(lst)):
        if lst[i][0] == '(' and lst[i][-1] == ')':
            lst.pop(i)
            if match_parens(lst) == 'Yes':
                return 'Yes'
            lst.insert(i, '()')

    return 'No'

