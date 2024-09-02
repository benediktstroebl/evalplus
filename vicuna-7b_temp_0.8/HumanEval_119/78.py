
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
    # check if lst has only open and close parens
    if any(c in ')' for c in lst):
        return 'No'

    # check if lst is a permutation of itself
    if len(lst) != 1:
        return 'No'

    # check if the number of open parens is the same as the number of close
    # parens
    open_count = len([c for c in lst if c == '('])
    close_count = len([c for c in lst if c == ')'])])
    if open_count != close_count:
        return 'No'

    # check if the last element of the list is a close paren
    if lst[-1] == ')':
        return 'Yes'

    # check if the first element of the list is an open paren
    if lst[0] == '(':
        return 'Yes'

    return 'No'
