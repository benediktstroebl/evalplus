
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

    # My solution
    # s = ''.join(lst)
    # stack = []
    # for char in s:
    #     if char == '(' or char == ')':
    #         if not stack:
    #             stack.append(char)
    #         elif char == '(':
    #             stack.append(char)
    #         elif char == ')':
    #             if stack[-1] == '(':
    #                 stack.pop()
    #             else:
    #                 stack.append(char)
    # return 'Yes' if stack == [] else 'No'
    #
    # Solution using stack data structure
    # s = ''.join(lst)
    # stack = []
    # for char in s:
    #     if char == '(':
    #         stack.append(char)
    #     else:
    #         if not stack:
    #             return 'No'
    #         else:
    #             stack.pop()
    # return 'Yes' if not stack else 'No'

    # Solution using stack data structure
    stack = []
    for i in lst:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()
    return 'Yes' if len(stack) == 0 else 'No'
