
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
    assert len(lst) == 2
    a = lst[0]
    b = lst[1]
    a_stack = []
    b_stack = []
    for i in a:
        if i == '(':
            a_stack.append(i)
        else:
            if len(a_stack) == 0:
                return 'No'
            else:
                a_stack.pop()

    for i in b:
        if i == ')':
            b_stack.append(i)
        else:
            if len(b_stack) == 0:
                return 'No'
            else:
                b_stack.pop()
    if len(a_stack) == 0 and len(b_stack) == 0:
        return 'Yes'
    else:
        return 'No'

