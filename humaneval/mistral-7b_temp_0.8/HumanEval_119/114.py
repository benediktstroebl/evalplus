
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

    # This function must return "Yes" if there's a way to make a good string,
    # and return "No" otherwise.
    # You may not assume the strings are non-empty.
    # You may not assume that the two strings are of the same length.
    # You may not assume that the strings are valid (you may want to check for
    # that before you call this function)
    # You may not mutate the input strings.
    # You may not use any built-in functions that check the length of a string.

    # Your function should be implemented in O(N) time, where N is the sum of
    # the length of the two input strings.
    # You should not modify any built-in Python functions.

    # solution
    if len(lst[0]) != len(lst[1]):
        return "No"
    else:
        if lst[0][0] == '(' and lst[1][-1] == ')':
            return "Yes"
        else:
            if lst[0][0] == '(':
                l
