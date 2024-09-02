
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

    parentheses = list(zip(lst[::2], lst[1::2]))

    if '(' in parentheses[0]:
        for c1, c2 in parentheses:
            if c1 == '(' and c2 == ')':
                parentheses.pop(0)

    return 'Yes' if parentheses else 'No'

