
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

    # TODO: Your code here
    # For every opening parenthesis, there must be a closing parenthesis.
    # So first, we count the opening and closing parenthesis and check for
    # equality. If not equal, return "No".
    open = 0
    close = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            open += 1
        elif lst[i] == ')':
            close += 1
    if open!= close:
        return "No"
    # Next, we need to check that all the closing parenthesis are after all
    # the opening parenthesis. If not, return "No".
    open_lst = []
    for i in range(len(lst)):
        if lst[i] == '(':
            open_lst.append(i)
        elif lst[i] == ')':
            # Check if there is an open_lst[-1] element,
            # and if the current index is smaller than that.
            if open_lst and open_lst[-1] < i:
                continue
            else:
                return "No"
    # If we get through both loops without returning "No",
    # return "Yes".
    return "Yes"
