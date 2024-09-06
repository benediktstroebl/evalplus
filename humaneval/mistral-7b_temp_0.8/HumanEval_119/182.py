
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

    # First, check if the parens of either of the strings are balanced.
    # If neither string is balanced, there's no way to make a good string.
    if not balance(lst[0]):
        return 'No'
    if not balance(lst[1]):
        return 'No'

    # If both strings are balanced, check if either of the strings is a substring of the other.
    # If one is a substring of the other, then the concatenation of the two strings
    # will be a good string.
    if lst[0] in lst[1]:
        return 'Yes'
    if lst[1] in lst[0]:
        return 'Yes'

    # If neither string is a substring of the other, then there's no way to make a good string.
    return 'No'
