
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
        return 'No'
    if len(lst) == 1:
        return 'Yes'
    if len(lst) > 1:
        for i in range(len(lst)):
            if i == 0 and lst[i] == '(' and lst[i + 1] == ')':
                lst[i] = 'Yes'
            elif i == 1 and lst[i] == '(' and lst[i + 1] == ')':
                lst[i + 1] = 'Yes'
            elif i < len(lst) - 2 and lst[i] == ')' and lst[i + 1] == '(' and lst[i + 2] == ')':
                lst[i + 1] = 'Yes'
            elif i < len(lst) - 1 and lst[i] == ')' and lst[i + 1] == '(':
                lst[i] = 'Yes'
            elif i < len(lst) - 1 and lst[i] == ')' and lst[i + 1] == ')':
                lst[i + 1] = 'Yes'
            elif i < len(lst) - 1 and lst[i] == '(' and lst[i + 1] == '(':
                lst[i] = 'Yes'
            elif i < len(lst) - 1 and lst[i] == '(' and lst[i + 1] == ')':
                lst[i] = 'Yes'
    if 'No' in lst:
        return 'No'
    if 'Yes' in lst:
        return 'Yes'

