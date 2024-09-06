
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

    
    if not lst:
        return 'Yes'
    
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i][0] == '(' and lst[j][0] == ')' and (lst[i][1:] in lst[j] or lst[j][1:] in lst[i]):
                lst[i], lst[j] = lst[j], lst[i]
                if match_parens(lst[:i] + lst[i+1:]):
                    return 'Yes'
                else:
                    lst[i], lst[j] = lst[j], lst[i]
    
    return 'No'
