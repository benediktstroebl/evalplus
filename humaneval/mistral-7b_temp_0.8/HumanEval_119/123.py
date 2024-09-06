
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

    # Check if each string is valid by itself
    if not is_valid_string(lst[0]) or not is_valid_string(lst[1]):
        return 'No'

    # Check if the last character of the first string is a '('
    if lst[0][-1] == '(':
        return 'No'

    # Check if the first character of the second string is a ')'
    if lst[1][0] == ')':
        return 'No'

    return 'Yes'

