
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
    # NOTE: O(n^2) solution is acceptable
    # NOTE: simpler to do this in O(n) but requires use of stack, which may
    # be overkill for this problem
    # NOTE: just use a `for` loop
    # NOTE: carry out the loop twice, once to check if stack is empty
    # after string, and the other time to actually parse string
    # NOTE: faster, but there's probably a better way
    from collections import deque
    # need to keep track of a stack because there's a recursion
    # structure here
    stack = deque([])
    # first, put all parentheses into stack
    for char in lst:
        stack.append(char)
    # now, check if all parentheses are balanced
    for char in lst:
        # if there's a close paren, pop the stack
        if char == ')':
            if stack.pop() != '(':
                return 'No'
    # if stack is empty at the end, it means all parentheses were balanced
    return 'Yes'
