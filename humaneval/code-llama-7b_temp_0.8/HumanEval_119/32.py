
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
    open_bracket = [')', '(']
    for item in lst:
        i = 0
        stack = []
        while i < len(item):
            stack.append(item[i])
            if (item[i] in open_bracket):
                stack.append(item[i])
                i += 1
            if (item[i] == ')'):
                if (stack[-1] == '('):
                    stack.pop()
                    i += 1
                else:
                    return 'No'
    return 'Yes'
