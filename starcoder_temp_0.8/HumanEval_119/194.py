
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
    # This is a list with only one element, so return the first element
    if len(lst) == 1:
        return lst[0]

    if lst[0] == lst[1]:
        return match_parens(lst[2:])

    if lst[0] == '(':
        return match_parens(lst[1:])
    elif lst[0] == ')':
        if match_parens(lst[2:]) == 'Yes':
            return match_parens(lst[1:])
        else:
            return 'No'

