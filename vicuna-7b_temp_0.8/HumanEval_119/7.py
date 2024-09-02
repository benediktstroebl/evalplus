
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
    # Check for empty list
    if not lst:
        return 'No'

    # If the first and second elements are not (), then return 'No'
    if not (lst[0] == '(' and lst[1] == ')'):
        return 'No'

    # Check if the third element is also (), then return 'No'
    if lst[2] == '(':
        return 'No'

    # If the third element is not (), check if the concatenation of the first
    # two elements and the third element is good.
    if (lst[0] + lst[1] + lst[2]) == '(())':
        return 'Yes'

    # If the concatenation is not good, check if the concatenation of the last
    # two elements is good.
    if (lst[1] + lst[2]) == '(())':
        return 'Yes'

    # If the last two elements are not good, return 'No'
    return 'No'
