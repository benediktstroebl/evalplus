
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
    if not lst[0]:
        return 'No'
    if lst[0]!= '(' or lst[-1]!= ')':
        return 'No'
    new_lst = [x[1:-1] for x in lst if x[0] == '(' and x[-1] == ')']
    return match_parens(new_lst)

