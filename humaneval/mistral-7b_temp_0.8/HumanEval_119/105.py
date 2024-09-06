
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
    lst_open = []
    lst_close = []

    for i in lst[0]:
        if i == '(':
            lst_open.append('(')
        else:
            lst_open.pop()

    for i in lst[1]:
        if i == ')':
            lst_close.append(')')
        else:
            lst_close.pop()

    if len(lst_open) == len(lst_close):
        return 'Yes'
    else:
        return 'No'

