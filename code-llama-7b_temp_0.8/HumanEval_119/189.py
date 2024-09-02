
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
    a = []
    b = []
    for i in lst[0]:
        a.append(i)
    for i in lst[1]:
        b.append(i)
    a = ''.join(a)
    b = ''.join(b)
    if len(a) > len(b):
        temp = a
        a = b
        b = temp
    if a == '':
        return 'Yes'
    if b == '':
        return 'No'
    if a == '(' * len(a) and b == ')' * len(b):
        return 'Yes'
    return 'No'
