
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
    # [::-1] reverse the list
    # use zip to iterate over the list and compare each character of the two strings
    # if the character in the first string is a left paren, then pop from the stack
    # and compare the popped paren with the right paren
    # if a mismatch occurs, return No
    # return Yes if there is no mismatch
    # initialize a stack
    stack = []
    for left, right in zip(lst, lst[::-1]):
        if left == '(' and right == ')':
            if stack:
                if stack[-1] == left:
                    stack.pop()
                else:
                    return 'No'
            else:
                stack.append(right)
        else:
            stack.append(right)
    if stack:
        return 'No'
    return 'Yes'

