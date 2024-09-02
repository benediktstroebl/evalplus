
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

    open_p = 0
    close_p = 0
    if len(lst) <= 1:
        return 'No'
    if lst[0] == '(' and lst[-1] == ')':
        for i in range(1, len(lst) - 1):
            if lst[i] == '(':
                open_p += 1
            elif lst[i] == ')':
                close_p += 1
            if open_p == close_p:
                return 'Yes'
        return 'No'
    else:
        return 'No'
