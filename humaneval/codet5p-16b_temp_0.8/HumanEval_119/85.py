
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

    
    if lst[0] == ')' or lst[1] == '(':
        return 'No'
    
    if len(lst[0]) == len(lst[1]):
        return 'Yes'
    
    if len(lst[0]) > len(lst[1]):
        return 'No'
    
    l = 0
    r = 1
    while r < len(lst[0]):
        if lst[0][l] == lst[1][r]:
            l += 1
            r += 1
        else:
            return 'No'
    return 'Yes'

