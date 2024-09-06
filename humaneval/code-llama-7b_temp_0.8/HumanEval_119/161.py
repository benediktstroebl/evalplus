
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
    i = 0
    j = len(lst) - 1
    while i < j:
        if lst[i] == '(' and lst[j] == ')':
            return 'Yes'
        if lst[i] == '(' and lst[j] == '(':
            i += 1
        elif lst[i] == ')' and lst[j] == ')':
            j -= 1
        else:
            return 'No'
    return 'Yes'
