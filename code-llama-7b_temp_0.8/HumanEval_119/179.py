
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

    # Validating inputs
    if not isinstance(lst, list):
        return 'Input must be a list'
    if not lst:
        return 'List cannot be empty'
    if len(lst) != 2:
        return 'List must have two elements only'

    # Creating variable to store stack
    stack = []

    # Iterating over the strings
    for i in lst:
        for x in i:
            if x == ')':
                # if the stack is empty return false
                if not stack:
                    return 'No'
                # if the last element in stack is '(' pop it
                if stack[-1] == '(':
                    stack.pop()
                # if the last element in stack is not '(' then the stack is not balanced return false
                else:
                    return 'No'
            else:
                # if the last element in stack is '(' push it
                stack.append('(')
    # if we are here the stack is balanced return yes
    return 'Yes'
