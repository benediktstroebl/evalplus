
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
    n = len(lst)
    if n == 0:
        return True
    elif n == 1:
        return lst[0].count('(') == lst[0].count(')')
    else:
        if (lst[0].count('(') == 0 or lst[0].count(')') == 0) and match_parens(lst[1:]):
            return True
        elif (lst[0].count('(') == 0 or lst[0].count(')') == 0) and not match_parens(lst[1:]):
            return False
        elif (lst[0].count('(') != lst[0].count(')')) and not match_parens(lst[1:]):
            return False
        elif (lst[0].count('(') == lst[0].count(')')) and match_parens(lst[1:]):
            return True
