
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
    par_dic = {'(': ')', ')': '(', '{': '}', '}': '{'}
    stack = []
    for par in lst:
        if len(par) != 0:
            if par[0] not in par_dic:
                return 'No'
            elif par_dic[par[0]] in stack:
                stack.pop()
            else:
                stack.append(par[0])
        else:
            if len(stack) == 0:
                return 'Yes'
            else:
                stack.pop()

    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'

