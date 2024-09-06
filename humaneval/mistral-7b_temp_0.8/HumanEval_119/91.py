
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
    # Return 'No'
    # if either string is empty or if the lengths are not equal.
    if not lst or len(lst) < 2 or len(lst[0]) != len(lst[1]):
        return 'No'

    # Initialize a list to store the result
    result = ['Yes']

    # Iterate through the strings and compare them
    for i in range(len(lst[0])):
        # If the current character is a '(', add it to the result
        if lst[0][i] == '(':
            result.append('Yes')
        # If the current character is a ')', add it to the result only if
        # the last character added was a '('
        elif lst[0][i] == ')' and result[-1] == 'Yes':
            result.append('Yes')
        # If the current character is a ')', add it to the result only if the
        # last character added was not a ')'
        elif lst[0][i] == ')' and result[-1] == 'No':
            result.append
