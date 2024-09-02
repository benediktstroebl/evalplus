
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
    # If both strings are empty, return 'Yes'.
    if lst[0] == '' and lst[1] == '':
        return 'Yes'
    # Create a stack and set the first string as the base string.
    stack = []
    base = lst[0]
    # If the base string is empty, return 'Yes'.
    if base == '':
        return 'Yes'
    # Loop through the string.
    for x in base:
        # If the current character is an opening bracket, push to stack.
        if x == '(':
            stack.append(x)
        # If the current character is a closing bracket and the stack is empty,
        # return 'No'.
        elif x == ')' and len(stack) == 0:
            return 'No'
        # If the current character is a closing bracket and the stack is not
        # empty, pop the stack and compare the popped item to the current
        # character.
        else:
            if x == stack[-1]:
                stack.pop()
            # If the popped item doesn't match the current character, return
            # 'No'.
            else:
                return 'No'
    # If the stack is not empty after looping through the string, return 'No'.
    if len(stack) != 0:
        return 'No'
    # Create a stack and set the second string as the base string.
    stack = []
    base = lst[1]
    # If the base string is empty, return 'Yes'.
    if base == '':
        return 'Yes'
    # Loop through the string.
    for x in base:
        # If the current character is an opening bracket, push to stack.
        if x == '(':
            stack.append(x)
        # If the current character is a closing bracket and the stack is empty,
        # return 'No'.
        elif x == ')' and len(stack) == 0:
            return 'No'
        # If the current character is a closing bracket and the stack is not
        # empty, pop the stack and compare the popped item to the current
        # character.
        else:
            if x ==
