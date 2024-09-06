
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
    # Open list
    open_list = []

    # Traverse the strings
    for i in lst:
        # Check if it is '('
        if i == '(':
            # Append the '(' to the open list
            open_list.append(i)
        # Check if it is ')'
        elif i == ')':
            # If the list is empty
            if not open_list:
                # Return no
                return 'No'
            # Remove the '(' from the list
            else:
                open_list.pop()

    # If the list is empty, return yes
    if not open_list:
        return 'Yes'
    # Otherwise, return no
    else:
        return 'No'
