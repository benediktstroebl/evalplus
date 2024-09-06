
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
    if not lst or len(lst) < 2:
        return 'No'

    if len(lst) == 2:
        return 'Yes' if parens_good(lst) else 'No'

    # split the list into two halves
    mid = len(lst) // 2
    left, right = lst[:mid], lst[mid:]
    # print(f'left={left} right={right}')

    # check if first half has closing paren that can be matched with open paren in second half
    for i in range(mid - 1, -1, -1):
        if left[i] == '(' and right[0] == ')':
            left[i] = right[0] = ''
            lst = left + right
            if parens_good(lst):
                return 'Yes'
            else:
                left[i] = '('
                right[0] = ')'
    return 'No'
