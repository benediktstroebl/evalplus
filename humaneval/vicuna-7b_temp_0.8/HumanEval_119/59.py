
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
    # check if the list is empty or not
    if not lst:
        return 'No'
    
    # for loop through the list
    for i in range(len(lst)):
        # check if the first string is empty or not
        if not lst[i]:
            continue
        # check if the second string is empty or not
        if not lst[i+1]:
            continue
        # check if the two strings are concatenated or not
        if lst[i] == lst[i+1]:
            continue
        # if they are not concatenated then they can't be good
        return 'No'
    # if they are concatenated then they can be good
    return 'Yes'
