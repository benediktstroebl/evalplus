
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

    
    if len(lst) == 1:
        return 'Yes'

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][0] == lst[j][0]:
                return 'Yes'
            if len(lst[i]) == 0 or len(lst[j]) == 0:
                return 'No'
            if lst[i][0] == lst[j][-1]:
                lst[i] = lst[i][1:]
                lst[j] = lst[j][:-1]
                if len(lst[i]) == 0 and len(lst[j]) == 0:
                    return 'Yes'
                elif len(lst[i]) == 0 or len(lst[j]) == 0:
                    return 'No'

    return 'Yes' if len(lst[i]) == 0 or len(lst[j]) == 0 else 'No'

