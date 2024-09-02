
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
    if len(lst) == 1:
        if lst[0].count('(') == 0 and lst[0].count(')') == 0:
            return 'Yes'
        else:
            return 'No'
    lst_to_check = []
    n = len(lst) // 2
    for x in lst:
        if x.count('(') > n or x.count(')') > n:
            return 'No'
        lst_to_check.append(x.count('('))
        lst_to_check.append(x.count(')'))
    if len(set(lst_to_check)) != 1:
        return 'No'
    return 'Yes'

