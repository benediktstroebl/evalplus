
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
    # split the strings and put them in an array
    # sort the array by first letter
    # iterate through the array
    # if the first item is an opening parenthesis, then open parenthesis is needed
    # if the first item is a closing parenthesis, then a closing parenthesis is needed
    # if the first item is an opening parenthesis and the second item is a closing parenthesis, then it's not possible
    # if the first item is a closing parenthesis and the second item is an opening parenthesis, then it's not possible
    # if the first item is a closing parenthesis and the second item is a closing parenthesis, then it's not possible
    # if the first item is an opening parenthesis and the second item is an opening parenthesis, then it's not possible
    # if the first item is a closing parenthesis and the second item is a closing parenthesis, then it's not possible
    # if the first item is an opening parenthesis and the second item is an opening parenthesis, then it's not possible
    # if the first item is an opening parenthesis and the second item is an opening parenthesis
