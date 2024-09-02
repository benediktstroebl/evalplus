
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
    # NOTE: this is a really hard problem
    if not lst or len(lst) == 1:
        return 'No'
    parens = {'(': ')', ')': '('}
    # NOTE: great idea to use stack
    stack = []
    for item in lst:
        if item in parens:
            stack.append(item)
        else:
            if not stack or parens[stack.pop()] != item:
                return 'No'
    return 'Yes' if not stack else 'No'

