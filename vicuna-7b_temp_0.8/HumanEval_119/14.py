
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
        return 'Yes'

    # Check if one of the strings is empty and the other one is not
    if len(lst) == 1:
        return 'No'

    # Check if both strings contain the same number of open and close parentheses
    if len(lst[0]) != len(lst[1]):
        return 'No'

    # Check if the number of open parentheses is equal to the number of close
    # parentheses in both strings
    if sum(lst[0].count(x) for x in ')(') != sum(lst[1].count(x) for x in ')(':
        return 'No'

    # Check if the strings can be concatenated in some way
    for i in range(len(lst[0]) - 1):
        # Check if the string is good
        if not match_parens(lst[0][i:i + len(lst[1])]):
            return 'No'

    return 'Yes'