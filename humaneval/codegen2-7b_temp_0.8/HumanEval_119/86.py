
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

    s1 = list(lst[0])
    s2 = list(lst[1])

    s1.reverse()
    s2.reverse()

    if len(s1) == 0:
        return 'No'
    if len(s2) == 0:
        return 'No'

    for i in range(0, len(s1)):
        if s1[i] == '(':
            s1.pop(i)

    for i in range(0, len(s2)):
        if s2[i] == ')':
            s2.pop(i)

    return 'Yes' if s1 == s2 else '
