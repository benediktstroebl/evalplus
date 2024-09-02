
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

    # handle empty strings
    if len(lst) == 0:
        return 'Yes'
    # check if strings are the same length
    if len(lst[0]) != len(lst[1]):
        return 'No'

    # iterate over list
    for i in range(len(lst[0])):
        # check each pair of parens, if they are the same, increment count
        if lst[0][i] == lst[1][i]:
            count += 1
        # if parens are different, decrement count
        else:
            count -= 1
        # if count ever becomes negative, return 'No'
        if count < 0:
            return 'No'

    # if count is 0 or greater, return 'Yes'
    if count == 0 or count > 0:
        return 'Yes'
    # if not, return 'No'
    else:
        return 'No'
