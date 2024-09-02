
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
    for i in range(len(lst)-1):
        if lst[i] == '(' and lst[i+1] == ')':
            # Balance one set of parentheses
            i += 2
            for j in range(i+1, len(lst)):
                if lst[j] == '(':
                    # If the next parenthesis is a '(' and the previous one is ')'
                    # we can balance it, since this is the first set of
                    # parenthesis in a string of a good type.
                    lst[i] = ')';
                    break
                elif lst[j] == ')':
                    # If the next parenthesis is ')' and the previous one is '('
                    # this is a different set of parenthesis, we can't balance it.
                    break
        elif lst[i] == '(':
            # We found a set of parenthesis, but they are not closed
            # so we can't balance them
            return 'No'
    return 'Yes'
