
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

    
    opened = []
    for el in lst:
        if el == '(' or el == ')':
            opened.append(el)
    count = 0
    for el in opened:
        if el == '(' or el == ')':
            if el == '(' and count == 0:
                count = 1
            elif el == ')' and count == 1:
                count = 0
        elif el == '(' and count == 1:
            return 'No'
    return 'Yes'

