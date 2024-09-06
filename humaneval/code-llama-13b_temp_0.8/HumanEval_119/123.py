
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

    # ['()(', ')']
    #  ^
    # ['(', '(', ')', ')']
    #
    # ['(', '(', ')', ')', '']
    #  ^
    # ['(', '(', ')', ')', ']
    #
    # [')', ')']
    #   ^
    # [')', ')', '']
    #   ^
    # [')', ']'
    #   ^
    # ['', ']']
    #   ^
    # ['']
    #   ^
    # []
    #   ^
    #
    # check if lst has an even length
    #
    # look at the first character in lst
    # if it is a '(' then append to stack
    # if it is a ')' then check if stack is empty
    #   if so, return 'No'
    #   else, pop from stack
    #
    # iterate through the rest of the characters
    #   if it is a '(', append to stack
    #   if it is a ')', check if stack is empty
    #     if so, return 'No'
    #     else, pop from stack
    #
    # if stack is empty then return 'Yes'
    # if stack is not empty then return 'No'

    if len(lst) % 2 != 0:
        return 'No'

    stack = []

    for char in lst:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()

    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'

