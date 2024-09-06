
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
    def loop(stack, lefts, rights, idx):
        if lefts and rights:
            for i in range(lefts.pop(), rights.pop() + 1):
                stack.append(i)
                loop(stack, lefts, rights, idx + 1)
                stack.pop()
            return True
        return False

    stack = []
    rights = 0
    for item in lst:
        if item == '(':
            rights += 1
        if item == ')':
            rights -= 1
        if item == '(' and rights < 0:
            return 'No'
        if item == ')' and rights != 0:
            return 'No'
        stack.append(item)
    return True if loop(stack, rights, rights, 0) else 'No'

