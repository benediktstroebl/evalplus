
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
    from collections import deque
    lst1 = deque()
    lst2 = deque()
    for elem in lst[0]:
        lst1.append(elem)
    for elem in lst[1]:
        lst2.append(elem)
    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[-1] == lst2[-1] == '(':
            lst1.pop()
            lst2.pop()
        elif lst1[-1] == '(' and lst2[-1] == ')':
            lst1.pop()
            lst2.pop()
        else:
            return 'No'
    return 'Yes'

