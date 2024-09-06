
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
    # Check for the special case of an empty list
    if not lst:
        return 'No'

    # If the list contains only one string, check if it's a valid closing
    # parenthesis to determine if the original string is valid
    lst = [i[0] if i[0] == ')'] else i
    if lst == '):':
        return 'Yes'

    # Check for the special case of a list with two opening parentheses
    if lst == '(':
        return match_parens(lst + [lst[1]])

    # If the list contains more than one string, check if all the strings
    # can be concatenated to form a valid string
    return 'Yes'