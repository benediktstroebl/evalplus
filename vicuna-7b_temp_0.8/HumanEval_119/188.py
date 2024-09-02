
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
    # Check if both strings have the same length
    if len(lst) != 2:
        return 'No'
    
    # Check if the first string has only open parentheses
    if not lst[0].endswith(')'):
        return 'No'
    
    # Check if the second string has only close parentheses
    if not lst[1].startswith('('):
        return 'No'
    
    # Check if the two strings can be concatenated
    if lst[0][:-1] != lst[1]:
        return 'No'
    
    # Check if all parentheses in the resulting string are balanced
    if not all(is_balanced(s) for s in lst[0][:-1]):
        return 'No'
    
    return 'Yes'
