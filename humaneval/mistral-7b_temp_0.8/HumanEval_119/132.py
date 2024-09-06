
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
    lst1, lst2 = lst
    if '(' not in lst2:
        return 'No'
    if ')' not in lst1:
        return 'No'

    lst1 = lst1.replace(')', '')
    lst1 = lst1.replace('(', '')
    lst2 = lst2.replace(')', '')
    lst2 = lst2.replace('(', '')

    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    if lst1 == lst2:
        return 'Yes'
    else:
        return 'No'
