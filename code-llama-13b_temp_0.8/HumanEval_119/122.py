
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
    def is_balanced(string):
        """
        checks if a string is balanced
        """
        if string[0] == '(' and string[-1] == ')':
            return True
        return False

    first = lst[0]
    second = lst[1]

    # return 'Yes' if both strings are balanced
    if is_balanced(first) and is_balanced(second):
        return 'Yes'

    # return 'Yes' if first string is not balanced and second string is balanced
    if not is_balanced(first) and is_balanced(second):
        return 'Yes'

    # return 'Yes' if first string is balanced and second string is not balanced
    if is_balanced(first) and not is_balanced(second):
        return 'Yes'

    # return 'No' if both strings are not balanced
    if not is_balanced(first) and not is_balanced(second):
        return 'No'

    return 'No'
