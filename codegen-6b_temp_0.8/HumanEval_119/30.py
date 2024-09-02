
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
    
    stack1 = []
    stack2 = []

    for paren in lst:
        if paren == '(':
            stack1.append(paren)
        elif paren == ')':
            if stack1:
                stack1.pop()
            elif stack2:
                return 'No'
            else:
                stack2.append(paren)

    return 'Yes' if not stack1 and not stack2 else 'No'

