
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
    # init stacks
    stack = []
    stack_open = []
    # append open parens to stack
    for val in lst:
        if val == '(':
            stack.append(val)
            stack_open.append(val)
        else:
            if len(stack_open) > 0:
                stack.append(val)
                stack_open.pop()

    # check if parens are balanced
    if len(stack)!= 0:
        return 'No'

    return 'Yes'

