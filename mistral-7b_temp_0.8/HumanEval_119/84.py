
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
    # Solution 1
    # Make the matching pairs in the first string, then if there is still any
    # open pair, add it to the second string. If any close pair matches,
    # remove it from the second string.
    # Repeat the process until there is no close or open pair left.
    # Return 'yes' if the remaining pairs are equal to each other.
    pairs_1 = []
    for idx, x in enumerate(lst[0]):
        if x == '(':
            pairs_1.append(idx)
    if pairs_1 and lst[1][pairs_1[0]] == '(':
        pairs_1.pop(0)
    else:
        return 'No'

    pairs_2 = []
    for idx, x in enumerate(lst[1]):
        if x == ')':
            pairs_2.append(idx)
    for idx in pairs_1:
        if lst[1][idx] == '(':
            pairs_2.pop(0)
    return 'Yes' if pairs_1 and pairs_2
