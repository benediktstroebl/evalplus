
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
    n = len(lst)
    assert n % 2 == 0, "String must have an even number of characters."
    # Now, let's try to check if we can form a valid string.
    # If we find an open paranthesis, we put it in a stack.
    # If we find a closed paranthesis, we try to pop the topmost open paranthesis
    # off the stack.
    # If at any time the stack is empty and we find a closed paranthesis,
    # then we return 'No'
    stack = []
    for char in lst:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'No'
            stack.pop()
    return 'Yes' if not stack else 'No'
