
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

    if len(lst) <= 1:
        return 'Yes'
    lst = list(map(list, lst))
    l1, l2 = [], []
    l3 = []
    for item in lst:
        if item.count('(') == item.count(')'):
            l1.append(item)
        else:
            l2.append(item)
    for item in l2:
        if item.count('(') == item.count(')'):
            l3.append(item)
    if l1 and l2:
        if l1[0].count('(') <= l3[0].count('('):
            l1, l3 = l3, l1
        l2 = l1 + l3
        return match_parens([list(map(list, zip(*item)))[1] for item in l2])
    return 'No'
