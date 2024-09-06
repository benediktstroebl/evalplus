
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
    l1 = lst[0]
    l2 = lst[1]
    if len(l1) + len(l2) != len(l1) + len(l2):
        return 'No'
    if l1 == ')' * len(l1) or l2 == ')' * len(l2):
        return 'No'
    i1 = 0
    i2 = 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] == '(' and l2[i2] == ')' and (i1 == 0 or l1[i1 - 1] != ')'):
            i1 += 1
            i2 += 1
        elif l1[i1] == ')' and l2[i2] == '(' and (i2 == 0 or l2[i2 - 1] != ')'):
            i1 += 1
            i2 += 1
        else:
            return 'No'
    return 'Yes'

