
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
    # FILL IN YOUR CODE HERE
    if len(lst) < 2:
        return False

    lst_1 = lst[0]
    lst_2 = lst[1]
    last_one = ''
    for i in lst_1:
        if i == '(':
            last_one = i

    for i in lst_2:
        if i == '(':
            return False

    if lst_1.count('(') == lst_1.count(')'):
        return True
    else:
        return False
