
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

    stack = []
    i = 0
    while i < len(lst[0]):
        if lst[0][i] == '(':
            stack.append(lst[0][i])
        elif lst[0][i] == ')' and stack:
            stack.pop()
        i += 1
    i = 0
    while i < len(lst[1]):
        if lst[1][i] == '(':
            stack.append(lst[1][i])
        elif lst[1][i] == ')' and stack:
            stack.pop()
        i += 1
    if not stack:
        return 'Yes'
    else:
        return 'No'

