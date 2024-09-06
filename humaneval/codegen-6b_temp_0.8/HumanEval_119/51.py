
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
        return ''

    DELIMITER = '('
    delimiter_stack = []

    for s in lst:
        curr = s
        if delimiter_stack and delimiter_stack[-1] == DELIMITER and curr == DELIMITER:
            delimiter_stack.pop()
            continue

        if curr == DELIMITER:
            delimiter_stack.append(DELIMITER)
        else:
            delimiter_stack.append(curr)

    if not delimiter_stack:
        return 'Yes'

    return 'No'

