
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
    lst1 = [int(i) for i in lst[0]]
    lst2 = [int(i) for i in lst[1]]
    if len(lst1) != len(lst2):
        return 'No'
    while len(lst1) != 0 and len(lst2) != 0:
        if lst1[-1] == 1 and lst2[-1] == 1:
            lst1.pop()
            lst2.pop()
        elif lst1[-1] == 1 and lst2[-1] == 0:
            return 'No'
        elif lst1[-1] == 0 and lst2[-1] == 1:
            return 'No'
        elif lst1[-1] == 1 and lst2[-1] == 0:
            lst1.pop()
        elif lst1[-1] == 0 and lst2[-1] == 1:
            lst2.pop()
    if len(lst1) != 0 or len(lst2) != 
