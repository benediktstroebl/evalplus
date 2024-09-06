
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

    # Solution 1:

    # if len(lst) != 2:
    #     return 'No'

    # s1, s2 = lst
    # if len(s1) == len(s2):
    #     return 'Yes'
    # if len(s1) > len(s2):
    #     s1, s2 = s2, s1

    # for i in range(len(s1)):
    #     if s1[i] == '(' and s2[i] == ')':
    #         continue
    #     else:
    #         return 'No'

    # return 'Yes'

    # Solution 2:

    if len(lst) != 2:
        return 'No'

    s1, s2 = lst
    if len(s1) != len(s2):
        return 'No'

    counter = 0

    for i in range(len(s1)):
        if s1[i] == '(':
            counter += 1
        elif s1
