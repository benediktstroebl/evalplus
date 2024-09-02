
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
    m, n = len(lst), len(lst[0])
    for i in range(m + n - 1):
        if lst[i] == '(' and lst[i+1] == ')':
            # they are closed parens, so it's not possible to concatenate them
            return 'No'
        if lst[i] == ')':
            # they are open parens, so it's not possible to concatenate them
            return 'No'
        if lst[i] == '(' and lst[i+m] == ')':
            # they are closed parens, so it's not possible to concatenate them
            return 'No'
        if lst[i+1] == '(' and lst[i+1+m] == ')':
            # they are open parens, so it's not possible to concatenate them
            return 'No'
    return 'Yes'

lst = ['(', '))', '(', ')', ')', '(', '(', ')', ')', '(', ')']
result = match_parens(lst)
