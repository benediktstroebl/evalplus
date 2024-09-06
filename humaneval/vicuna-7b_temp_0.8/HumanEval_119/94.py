
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
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == '(' and lst[j] == ')':
                # Concatenate the substrings up to the open parenthesis
                sublst = lst[:i] + lst[j + 1:]
                # Replace the open parenthesis with a concatenated substring
                lst[i:j] = sublst
                # Check if the resulting string is good
                if is_balanced(lst) == 'Yes':
                    return 'Yes'
    return 'No'