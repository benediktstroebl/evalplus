
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
    # Loop through the list and check if concatenating the two strings in
    # some order will result in a good string.
    for i in range(len(lst)-1):
        if lst[i] == '(' and lst[i+1] == ')':
            # If the first two characters are a parenthesis, check if they can
            # be concatenated to form a good string.
            if lst[i+2] == '(' or lst[i+2] == ')':
                # If they can, return 'Yes'
                return 'Yes'
            else:
                # If they can't, return 'No'
                return 'No'
        elif lst[i] == ')':
            # If the last character is a parenthesis, check if it can be
            # concatenated with the first character to form a good string.
            if lst[0] == '(':
                # If it can, return 'Yes'
                return 'Yes'
            else:
                # If it can't, return 'No'
                return 'No'
    # If none of the above conditions are met, return 'No'
    return 'No'
