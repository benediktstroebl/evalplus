
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
    # My solution
    # Set a count to 0.
    # Loop through the first string
    # If a '(' is found, add 1 to the count
    # If a ')' is found, subtract 1 from the count
    # If the count is ever below 0, return 'No'
    # If the count is ever above 0, return 'Yes'
    # If the count is ever equal to 0, keep looping.
    # If the loop is done without returning, return 'Yes'
    count = 0
    for string in lst:
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count < 0:
                return 'No'
            elif count > 0:
                return 'Yes'
    return 'Yes'
