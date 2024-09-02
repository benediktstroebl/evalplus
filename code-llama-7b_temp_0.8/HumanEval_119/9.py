
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
    open_pars = 0
    closed_pars = 0
    for i in lst:
        if i == '(':
            open_pars += 1
        else:
            closed_pars += 1
        if closed_pars > open_pars:
            return 'No'
    if closed_pars == open_pars:
        return 'Yes'
    else:
        return 'No'

