
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
    # Create a variable to store the parentheses
    # that are not matched
    unmatched = []
    # Iterate through each character in lst
    # If the character is an open paren,
    # add it to unmatched
    # If the character is a closed paren,
    # if unmatched is empty, return No
    # If unmatched has an open paren, remove it
    # If unmatched is empty, return Yes
    for i in lst:
        if i == '(':
            unmatched.append('(')
        elif i == ')':
            if unmatched == []:
                return 'No'
            elif unmatched[-1] == '(':
                unmatched.pop()
            if unmatched == []:
                return 'Yes'
    # If unmatched is not empty return No
    if unmatched != []:
        return 'No'
