
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
    lst1 = []
    lst2 = []
    for i in lst[0]:
        lst1.append(i)
    for i in lst[1]:
        lst2.append(i)

    if len(lst1) + len(lst2) == 0:
        return 'Yes'
    else:
        if lst1[0] == '(' and lst2[0] == ')':
            lst1.pop(0)
            lst2.pop(0)
            return match_parens([lst1, lst2])
        elif lst1[0] == ')' and lst2[0] == '(':
            lst1.pop(0)
            lst2.pop(0)
            return match_parens([lst1, lst2])
        elif lst1[0] == ')' and lst2[0] == ')' or lst1[0] == '(' and lst2[0] == '(':
            lst1.pop(0)
            lst2.pop(0)
            return match_parens([lst1, lst2])
        elif lst1[0] == ')' and lst2[0] == '(':
            lst1.pop(0)
            lst2.pop(0)
            return match_parens([lst2, lst1])
        elif lst1[0] == '(' and lst2[0] == ')':
            lst1.pop(0)
            lst2.pop(0)
            return match_parens([lst2, lst1])
        else:
            return 'No'

