
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
    # Open parens = 1, close parens = 2
    stack = []
    for char in lst[0] + lst[1]:
        if char == "(":
            stack.append("open")
        elif char == ")":
            stack.append("close")
        else:
            continue
    if len(stack) % 2 != 0:
        return "No"
    for i in range(len(stack)//2):
        if stack[i] == "close" and stack[len(stack) - 1 - i] == "open":
            continue
        else:
            return "No"
    return "Yes"
