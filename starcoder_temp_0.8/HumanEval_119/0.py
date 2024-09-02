
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

    assert isinstance(lst, list)
    assert all(isinstance(item, str) for item in lst)
    assert all(item in '()' for item in ''.join(lst))
    assert len(lst) == 2
    assert len(set(lst)) == 2

    first, second = lst
    open_parens = 0
    for item in first + second:
        if item == '(':
            open_parens += 1
        elif item == ')':
            open_parens -= 1
        if open_parens < 0:
            return 'No'
    return 'Yes' if open_parens == 0 else 'No'
