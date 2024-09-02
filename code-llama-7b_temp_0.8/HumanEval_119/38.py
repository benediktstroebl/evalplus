
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
    open_parens = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    close_parens = {open_parens[i]: i for i in range(len(open_parens))}
    if not set(close_parens) == set(set(lst[0] + lst[1])):
        return 'No'
    stack = []
    for char in lst[0] + lst[1]:
        if char in open_parens:
            stack.append(char)
        elif char in close_parens:
            if stack and stack[-1] == open_parens[close_parens[char]]:
                stack.pop()
            else:
                return 'No'
    return 'Yes' if not stack else 'No'
