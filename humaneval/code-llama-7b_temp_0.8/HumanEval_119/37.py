
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
    # Edge Cases
    if lst == []:
        return 'Yes'
    # Method 1
    # # Check both strings with opening parens
    # opening_paren_counts = []
    # for element in lst:
    #     opening_paren_counts.append(element.count('('))
    # # Check both strings with closing parens
    # closing_paren_counts = []
    # for element in lst:
    #     closing_paren_counts.append(element.count(')'))
    # # Compare opening and closing parens
    # if opening_paren_counts > closing_paren_counts:
    #     return 'Yes'
    # else:
    #     return 'No'

    # Method 2
    # Convert strings to lists
    lst = list(map(list, lst))

    # Return 'No' if the opening parens don't equal the closing parens
    if len(lst[0]) != len(lst[1]):
        return 'No'

    # Return 'Yes' if the strings are empty
    if len(lst[0]) == 0:
        return 'Yes'

    # Compare the last elements of the two strings
    if lst[0][-1] == '(' and lst[1][-1] == ')':
        return 'Yes'
    elif lst[0][-1] == ')' and lst[1][-1] == '(':
        return 'No'
    else:
        # Remove the last characters
        lst[0].pop()
        lst[1].pop()
        # Recurse
        match_parens(lst)

