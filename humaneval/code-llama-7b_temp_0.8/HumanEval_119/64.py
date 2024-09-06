
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
    # stack 1st element, stack 2nd element
    # pop from stack
    # if the second element is not a close paren,
    #   push the second element to the stack
    # else
    #   if the second element is a close paren and
    #   the first element is an open paren,
    #       pop from the stack
    #   else
    #       return No
    #   pop from the stack
    # return Yes
    stack = []
    for elem in lst:
        if elem == '(':
            stack.append(elem)
        else:
            if elem == ')':
                stack.pop()
            else:
                return 'No'
    return 'Yes'


