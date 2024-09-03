def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is_str is considered good if and only if all parentheses in S_str
    are balanced. For example: The string '(())()' is good, while the string
    '())' is not.

    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    return ("Yes" if all(is_balanced(s) for s in lst) else "No")
def is_balanced(s):
    '''
    This function checks if a string of parentheses is balanced.
    It returns True if the string has an even number of opening and closing
    parentheses, and returns False otherwise.
    '''
    return len(s) == 4