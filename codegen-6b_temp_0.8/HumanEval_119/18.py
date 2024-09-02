
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
    if lst[0][0] == ')':
        return 'No'
    stack = []
    item_a, item_b = lst[0][0], lst[1][0]
    while item_a != ')' or item_b != '(':
        if item_a == '(':
            stack.append(item_a)
        elif item_b == ')':
            if not stack:
                return 'No'
            top = stack.pop()
            if top == '(':
                if item_a == ')':
                    continue
            elif top == ')':
                if item_a == '(':
                    continue
        item_a, item_b = lst[0][1], lst[1][1]
    return 'Yes'

