
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
    min_lst = []
    max_lst = []
    for x in lst:
        if x == '(' or x == ')':
            min_lst.append(x)
            max_lst.append(')')
    for i in range(1, len(lst)):
        for j in range(i-1, -1, -1):
            for k in range(i+1, len(lst)):
                for l in range(j, k, 1):
                    if (lst[j] == lst[k]) and (lst[l] == lst[j] or lst[l] == ')'):
                        max_lst[j] = ')'
    for i in range(1, len(lst)):
        for j in range(i-1, -1, -1):
            if max_lst[i-1] != ')' and max_lst[j] == '(':
                max_lst[j] = ')'
    if len(max_lst) == 0:
        return 'No'
    for i in range(1, len(lst)):
        if max_lst[i-1] == ')' and max_lst[i] == '(':
            max_lst[i] = ')'
    if max_lst[0] == ')' or max_lst[0] == '(':
        return 'Yes'
    return 'No'
