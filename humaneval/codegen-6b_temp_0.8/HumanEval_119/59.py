
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
    if not lst:
        return 'Yes'

    stack, p1, p2 = [], len(lst[0]), len(lst[1])
    stack.append(lst[0][p1])

    for i in range(1, len(lst[0])):
        while len(stack) > 0 and lst[0][i] == ')' and stack[-1] == '(':
            stack.pop()
            if len(stack) == 0:
                return 'Yes'
            else:
                stack.append(lst[0][i])
        stack.append(lst[0][i])

    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'

