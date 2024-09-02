
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
    # find the starting index of the opening brackets in the first string
    first_idx = lst[0].find('(')

    # if the second string is empty or the index of the starting bracket is -1
    # or the first bracket is not balanced with the closing bracket
    # the answer is no
    if not lst[1] or first_idx == -1 or not match_parens_helper(lst, 0, 1, first_idx):
        return 'No'
    return 'Yes'
