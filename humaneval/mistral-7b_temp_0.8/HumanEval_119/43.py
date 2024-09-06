
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

    # Check if both lists have the same length
    if len(lst) != 2:
        return "No"

    # Check if both lists contain only open and close parentheses
    if not all(c in '()' for c in lst[0]) or not all(c in '()' for c in lst[1]):
        return "No"

    # Count the number of open and close parentheses in each list
    count_open = sum(c == '(' for c in lst[0])
    count_close = sum(c == ')' for c in lst[0])
    count_open_1 = sum(c == '(' for c in lst[1])
    count_close_1 = sum(c == ')' for c in lst[1])

    # Check if both lists contain the same number of open and close parentheses
    if count_open != count_close or count_open_1 != count_close_1:
        return "No"

    # Check if the concatenation of the two lists contains balanced parentheses
