
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
    lst = lst[::-1]
    for i in range(len(lst)):
        if lst[i] == '(':
            if i!= 0 and lst[i - 1]!= '(':
                lst[i] = '*'
        elif lst[i] == ')':
            if i!= len(lst) - 1 and lst[i + 1]!= ')':
                lst[i] = '*'
    if '*' not in lst:
        return 'Yes'
    else:
        return '
