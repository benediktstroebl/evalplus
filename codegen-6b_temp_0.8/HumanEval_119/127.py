
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
    num_brackets = 0
    for pair in lst:
        for bracket in pair:
            if bracket == '(':
                num_brackets += 1
            elif bracket == ')':
                num_brackets -= 1
            if num_brackets < 0:
                return 'No'
    return 'Yes' if num_brackets == 0 else 'No'

