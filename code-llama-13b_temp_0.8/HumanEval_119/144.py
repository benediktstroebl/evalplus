
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
    # counter = 0
    # if lst[0] == '(' and lst[1] == ')':
    #     return 'Yes'
    # else:
    #     for i in lst:
    #         if i == '(':
    #             counter += 1
    #         if i == ')':
    #             counter -= 1
    #     if counter != 0:
    #         return 'No'
    #     else:
    #         return 'Yes'
    # return 'No'

    res = []
    for i in lst:
        if i == '(':
            res.append('(')
        else:
            if res and res[-1] == '(':
                res.pop()
            else:
                res.append(')')
    if len(res) == 0:
        return 'Yes'
    return 'No'

