
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
    # check if the two lists have equal number of brackets
    if len(lst) != len(lst[1]):
        return 'No'
    # match left and right brackets, if all match then it's good
    l_stack = []
    r_stack = []
    for i in lst[0]:
        if i == '(':
            l_stack.append(i)
        else:
            r_stack.append(i)
    for i in lst[1]:
        if i == '(':
            l_stack.append(i)
        else:
            r_stack.append(i)
    for i in range(len(r_stack)):
        if l_stack[i] != r_stack[i]:
            return 'No'
    return 'Yes'

