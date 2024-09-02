
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

    # Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
    if len(lst[0]) > len(lst[1]):
        lst = lst[::-1]

    l = lst[0]
    r = lst[1]

    l_i = 0
    r_i = 0

    while l_i < len(l) and r_i < len(r):
        if l[l_i] == r[r_i]:
            l_i += 1
            r_i += 1
        else:
            l_i += 1

    if l_i == len(l) and r_i == len(r):
        return 'Yes'
    else:
        return 'No'
