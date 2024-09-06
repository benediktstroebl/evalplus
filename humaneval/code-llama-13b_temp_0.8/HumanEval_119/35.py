
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
    # 1) Do the lists have the same length?
    # 2) Does the first list have a number of closing parentheses equal
    #    to the number of opening parentheses?
    # 3) Does the second list have a number of opening parentheses equal
    #    to the number of closing parentheses?
    # 4) If any of the above is not true, return 'No'
    # 5) Check to see if the first list has at least one item
    # 6) If it does, then we can safely pop the first item from the first list
    # 7) If it is an opening parenthesis, then we can safely pop the first
    #    item from the second list
    # 8) If it is a closing parenthesis, then we can safely pop the first
    #    item from the second list
    # 9) If the first item in the first list is a closing parenthesis, then
    #    the parenthesis is not balanced
    # 10) Otherwise, the parenthesis is balanced
    # 11) Repeat steps 5 through 10 until the first list is empty
    # 12) If the second list is not empty, then there is an imbalance
    # 13) Return 'Yes' if the list is empty and 'No' otherwise
    return 'Yes' if match_parens_2(lst) else 'No'
