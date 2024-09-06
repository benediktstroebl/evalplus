
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

    assert lst[0] == '(' or lst[0] == ')'
    assert lst[1] == '(' or lst[1] == ')'
    assert len(lst[0]) == len(lst[1])

    if len(lst[0]) == 1:
        return 'Yes'

    s = lst[0] + lst[1]
    if len(s) % 2 == 1:
        return 'No'

    stack = []
    for c in s:
        if c == ')' and len(stack) == 0:
            return 'No'
        if c == ')':
            stack.pop()
        else:
            stack.append(c)
    if len(stack)!= 0:
        return 'No'

    return 'Yes'

