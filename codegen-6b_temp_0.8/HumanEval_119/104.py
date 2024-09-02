
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
    elif len(lst) == 1:
        return 'Yes' if lst[0] == ')' else 'No'
    elif len(lst) == 2:
        if lst[0] == ')' and lst[-1] == '(':
            return 'Yes'
        elif lst[0] == ')' and lst[-1] == ')':
            return 'No'
        else:
            return 'Yes' if lst[-1] == ')' else 'No'
    else:
        t1 = match_parens(lst[1:])
        t2 = match_parens(lst[:-1])
        if (t1 == 'No' and t2 == 'No') or t1 == 'Yes' and t2 == 'Yes':
            return 'Yes'
        elif t1 == 'Yes' and t2 == 'No':
            return 'Yes'
        else:
            return 'No'

