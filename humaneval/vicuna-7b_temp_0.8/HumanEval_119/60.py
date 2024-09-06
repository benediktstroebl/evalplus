
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
    # Check if both strings are empty
    if not lst:
        return 'No'

    # Check if the first string is ')'
    if lst[0] == ')':
        # Check if the second string is empty
        if not lst[1:]:
            return 'No'
        # Check if the second string is '(', return 'No'
        elif lst[1] == '(':
            return 'No'
        # Check if the second string is a valid string, return 'Yes'
        else:
            return 'Yes'

    # Check if the first string is '('
    if lst[0] == '(':
        # Check if the second string is empty
        if not lst[1:]:
            return 'No'
        # Check if the second string is ')', return 'No'
        elif lst[1] == ')':
            return 'No'
        # Check if the second string is a valid string, return 'Yes'
        else:
            return 'Yes'