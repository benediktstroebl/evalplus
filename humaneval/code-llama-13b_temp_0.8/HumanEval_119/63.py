
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
    def check(one):
        # False means something is wrong
        # True means no mistakes
        return one.count('(') == one.count(')')
    if check(lst[0]) and check(lst[1]):
        # make sure both are balanced
        return 'Yes'
    elif not check(lst[0]) or not check(lst[1]):
        # at least one is unbalanced
        return 'No'

    # otherwise, lets concatenate them and see
    res = lst[0] + lst[1]
    return 'Yes' if check(res) else 'No'

