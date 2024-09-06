
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
    left_chars = '({['
    right_chars = ')}]'

    if len(lst) % 2 == 1:
        return 'No'

    left_balance = 0
    right_balance = 0

    for char in lst[::-1]:
        if char in left_chars:
            left_balance += 1
        elif char in right_chars:
            right_balance += 1

        if left_balance == right_balance:
            return 'Yes'

    return 'No
