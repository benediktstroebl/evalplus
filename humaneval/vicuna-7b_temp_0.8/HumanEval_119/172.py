
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
    if not any(lst):
        return 'No'
    # Iterate through all the possible combinations of the strings in the list
    for i in range(len(lst)):
        # Create a copy of the list
        lst = lst[:i] + lst[i+1:]
        # Recursively check if a good string can be made from the updated list
        if match_parens(lst):
            return 'Yes'
    return 'No'