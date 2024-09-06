
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
    p_list = []
    for p in lst:
        for i in p:
            if i == '(':
                p_list.append(i)
            elif i == ')':
                if len(p_list) == 0:
                    return 'No'
                else:
                    p_list.pop(-1)
            else:
                continue
        if len(p_list) == 0:
            return 'Yes'
        else:
            p_list = []
            continue

