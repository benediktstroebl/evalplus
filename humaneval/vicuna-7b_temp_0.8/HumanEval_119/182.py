
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
    if not lst:
        return 'No'
    left, right = lst[0], lst[1]
    while left or right:
        if left:
            left = left.next
        if right:
            right = right.prev
        if left and right:
            if left.type != 'CLOSE':
                return 'No'
        if left and right.type == 'OPEN':
            if left.type == 'CLOSE':
                return 'No'
        if right.type == 'CLOSE':
            return 'No'
        left, right = right, left

    return 'Yes'
