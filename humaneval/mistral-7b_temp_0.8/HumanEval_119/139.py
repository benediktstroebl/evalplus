
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
    # first we check if we have the same number of opens and closes
    # if not, return false
    if sum([i for i in lst if i == '(']) != sum([i for i in lst if i == ')']):
        return False
    # check if we have an open not followed by a close
    # and a close not followed by an open
    if '(' in lst and ')' not in lst or ')' in lst and '(' not in lst:
        return False
    # if the above two conditions are met, check if we have a string of
    # closes and opens that are not balanced
    for i in lst:
        if i == '(' and ')' in lst[-1:]:
            lst = lst[:-1]
        if i == ')' and '(' in lst[-1:]:
            lst = lst[:-1]
    if not lst:
        return True
    return False
