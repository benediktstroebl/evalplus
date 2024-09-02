
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
    bal = [0] * len(lst)
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] not in ['(', ')']:
            continue
        c = lst[i]
        if c == '(':
            bal[i] = 1
        else:
            bal[i] = -1
        for j in range(i - 1, -1, -1):
            if lst[j] == '(':
                bal[i] += bal[j]
            else:
                bal[i] -= bal[j]
            if bal[j] == 0:
                break
        if bal[i] == 0:
            return 'Yes'
    return 'No'

