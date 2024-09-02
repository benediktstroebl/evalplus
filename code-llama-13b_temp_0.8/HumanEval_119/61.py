
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

    def match(a, b):
        return a == ')' and b == '(' or a == '(' and b == ')'

    def is_good(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                if stack[-1] != '(':
                    return False
                stack.pop()
        return stack == []

    s = lst[0] + lst[1]
    if is_good(s):
        return 'Yes'
    s = lst[1] + lst[0]
    if is_good(s):
        return 'Yes'
    return 'No'

