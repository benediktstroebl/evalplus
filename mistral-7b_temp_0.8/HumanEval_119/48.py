
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
    # your code here
    assert len(lst) == 2
    open_p = lst[0].count("(")
    close_p = lst[0].count(")")
    open_p2 = lst[1].count("(")
    close_p2 = lst[1].count(")")
    if open_p != close_p and open_p2 != close_p2:
        return "No"
    else:
        return "Yes"
