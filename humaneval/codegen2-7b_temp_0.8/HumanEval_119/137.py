
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
    balanced_count = 0
    for item in lst:
        if item == '(':
            balanced_count += 1
        elif item == ')':
            balanced_count -= 1
            if balanced_count < 0:
                return 'No'
    if balanced_count == 0:
        return 'Yes'
    return 'No
