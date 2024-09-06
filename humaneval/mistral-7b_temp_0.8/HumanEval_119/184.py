
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
    def is_balanced(str):
        stack = []
        for c in str:
            if c == '(':
                stack.append(')')
            elif c == ')' and stack:
                stack.pop()
            elif not stack:
                return False
        return not stack
    return 'Yes' if is_balanced(lst[0]) and is_balanced(lst[1]) else 'No'



