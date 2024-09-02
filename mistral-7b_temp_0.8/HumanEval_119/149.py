
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
    first_str = lst[0]
    second_str = lst[1]

    if len(first_str) != len(second_str):
        return "No"

    # first_str = '()(('
    # second_str = ')(())'

    for i in range(len(first_str)):
        if first_str[i] == '(' and second_str[i] == ')':
            continue
        elif first_str[i] == '(' and second_str[i] == '(':
            first_str = first_str[:i] + first_str[i+1:]
            second_str = second_str[:i] + second_str[i+1:]
        elif first_str[i] == ')' and second_str[i] == ')':
            first_str = first_str[:i] + first_str[i+1:]
            second_str = second_str[:i] + second_str[i+1:]
        else:
            return "No"

    if first_str
