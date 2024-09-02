
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

    
    if len(lst)!= 2:
        return 'No'
    s1 = lst[0]
    s2 = lst[1]
    
    if s1[-1]!= s2[0]:
        return 'No'
    
    while s1 and s2:
        if s1[-1] == s2[0]:
            s1 = s1[:-1]
            s2 = s2[1:]
        else:
            return 'No'
    
    if s1 == '' and s2 == '':
        return 'Yes'
    return 'No'
    
