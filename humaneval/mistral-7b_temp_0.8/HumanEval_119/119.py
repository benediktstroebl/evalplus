
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
    s1, s2 = lst
    s1_open, s1_close = 0, 0
    s2_open, s2_close = 0, 0
    for c in s1:
        if c == '(':
            s1_open += 1
        else:
            s1_close += 1
    for c in s2:
        if c == '(':
            s2_open += 1
        else:
            s2_close += 1
    if s1_open == s1_close and s2_open == s2_close:
        return 'Yes'
    else:
        return 'No'

