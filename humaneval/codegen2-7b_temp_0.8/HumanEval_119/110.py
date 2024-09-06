
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
    open_list = [')', '(']
    close_list = [')', '(']
    stack = []

    for i in lst[1]:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            if stack and stack[-1] == open_list[close_list.index(i)]:
                stack.pop()
            else:
                return 'No'

    return 'Yes'
