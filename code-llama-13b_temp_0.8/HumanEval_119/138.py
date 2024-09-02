
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

    # Find first paren in each string, in each case the first or last is the one.
    first_open, first_closed = None, None
    for i, paren in enumerate(lst[0]):
        if paren == '(':
            first_open = i
        elif paren == ')':
            first_closed = i

    for i, paren in enumerate(lst[1]):
        if paren == '(':
            first_open = i
        elif paren == ')':
            first_closed = i

    # Now match them up
    if (first_open == first_closed) and first_open is not None:
        return 'Yes'

    return 'No'
