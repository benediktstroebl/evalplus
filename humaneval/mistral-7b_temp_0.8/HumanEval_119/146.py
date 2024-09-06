
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

    # initialize two variables to keep track of open and close parentheses
    open_count = 0
    close_count = 0

    # loop through both strings and check if the open and close parentheses
    # match
    for char in lst[0]:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count != 0:
                open_count -= 1
            else:
                close_count += 1

    # if the count of both open and close parentheses are equal, then it is
    # possible to concatenate the strings in some order that the resulting
    # string will be good
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'
