
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
    l1, l2 = lst
    if len(l1) != len(l2):
        return 'No'
    l3 = [0] * len(l1)
    for i, j in zip(l1, l2):
        if i == '(':
            l3[j] = -1
        else:
            l3[j] = 1
    for i in range(len(l3)):
        if l3[i] < 0 and l3[i] + 1 not in l3:
            return 'No'
    return 'Yes'
