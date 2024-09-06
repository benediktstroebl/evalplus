
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
    def is_balanced(string):
        stack = []
        for i in range(len(string)):
            if string[i] == ')':
                if not stack:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string[i])
        return not stack

    lst[1] += lst[0]
    if is_balanced(lst[1]):
        return 'Yes'
    return 'No'

