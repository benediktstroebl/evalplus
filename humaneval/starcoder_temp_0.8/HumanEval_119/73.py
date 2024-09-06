
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
    # make the first string to a stack
    # make a second string to a stack
    # take the first character from the first and second strings
    # if the first character is ')', pop the top element from the first string stack
    # if the first character is '(', pop the top element from the second string stack
    # if both stacks are empty, return 'Yes'
    # else return 'No'
    pass

