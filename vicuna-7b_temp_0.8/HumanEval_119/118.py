
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
    # no parentheses
    if not lst:
        return 'No'

    # one pair
    elif len(lst) == 1:
        # no more pairs to add
        if not lst[0]:
            return 'No'

        # add the first element and return 'Yes'
        return 'Yes'

    # two pairs
    else:
        # no way to make a good string
        return 'No'
