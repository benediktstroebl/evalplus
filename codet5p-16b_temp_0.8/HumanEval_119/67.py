
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

    def balanced(s):
        s = list(s)
        stack = []
        for paren in s:
            if paren == '(':
                stack.append(paren)
            elif paren == ')':
                if len(stack) == 0 or stack.pop()!= '(':
                    return False
        return len(stack) == 0

    for i in range(len(lst)):
        s1 = lst[i]
        s2 = lst[len(lst)-1-i]
        if not balanced(s1) or not balanced(s2):
            return 'No'
    return 'Yes'
