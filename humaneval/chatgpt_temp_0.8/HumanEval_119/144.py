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
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]
    # Use a stack to keep track of open parentheses
    stack = []
    # Iterate through the concatenated string
    for char in s:
        if char == '(':
            # Add open parentheses to the stack
            stack.append(char)
        else:
            # If the stack is empty or the top element is not an open
            # parenthesis, the string is not balanced
            if not stack or stack[-1] != '(':
                return 'No'
            # Otherwise, pop the top element from the stack
            stack.pop()
    # If the stack is empty, the string is balanced
    if not stack:
        return 'Yes'
    # Otherwise, the string is not balanced
    return 'No'
