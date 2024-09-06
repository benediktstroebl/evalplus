
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
    def is_balanced(parens):
        """Check if parens is balanced."""
        opens = 0
        for char in parens:
            if char == '(':
                opens += 1
            elif char == ')':
                opens -= 1
            if opens < 0:
                return False
        return opens == 0
    if not lst:
        return 'Yes'
    for i in range(len(lst)):
        if is_balanced(lst[i] + lst[-1]):
            lst[i] += lst[-1]
            lst.pop()
            return match_parens(lst)
    return 'No'
