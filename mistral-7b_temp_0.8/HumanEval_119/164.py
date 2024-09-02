
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
    str1 = lst[0]
    str2 = lst[1]

    if str1 == str2:
        return 'Yes'

    l = len(str1)
    k = 0
    for i in range(len(str1)):
        if str1[i] == '(':
            k += 1
        else:
            k -= 1
        if k < 0:
            return 'No'

    if k == 0:
        return 'Yes'

    l = len(str2)
    k = 0
    for i in range(len(str2)):
        if str2[i] == '(':
            k += 1
        else:
            k -= 1
        if k < 0:
            return 'No'

    if k == 0:
        return 'Yes'
    else:
        return 'No'
