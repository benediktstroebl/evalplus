
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
    from collections import deque
    def balanced(parens):
        # popleft and appendright - more efficient, no need to copy
        # O(n) for n = len(parens)
        stack = deque()
        for parent in parens:
            if parent == '(':
                stack.appendleft(parent)
            elif parent == ')':
                if not stack or stack.popleft() != '(':
                    return False
        return not stack # empty stack
    #
    if not lst or len(lst) != 2:
        return 'No'
    #
    return 'Yes' if balanced(lst[0]) and balanced(lst[1]) else 'No'
