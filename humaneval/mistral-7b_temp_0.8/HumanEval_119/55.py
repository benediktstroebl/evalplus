
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
    # if any of the strings are empty, the strings cannot be matched
    if any(string == '' for string in lst):
        return 'No'
    if len(lst[0]) != len(lst[1]):
        return 'No'
    # for each string, use a counter to keep track of how many '(' and ')'
    # there are
    count = { '(':0, ')' :0}
    # for each character in the first string
    for char in lst[0]:
        # if char is a '(', increment '(' counter
        if char == '(':
            count['('] += 1
        # if char is a ')', increment ')' counter
        else:
            count[')'] += 1
    # for each character in the second string
    for char in lst[1]:
        # if char is a '(', increment '(' counter
        if char == '(':
            count['('] += 1
        # if char is a ')', increment ')' counter
        else:
            count[')'] += 1
    #
