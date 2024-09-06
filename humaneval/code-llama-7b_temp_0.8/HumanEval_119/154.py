
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
    # take a look at the following link
    # https://stackoverflow.com/questions/3384401/check-if-a-string-is-a-valid-bracket-sequence

    def valid_parentheses(parens):
        """
        Return True if the string has balanced parentheses.
        """
        # if there is no parentheses in the string, return True
        if parens.find('(') == -1 and parens.find(')') == -1:
            return True

        # make a list of parentheses
        stack = []
        for paren in parens:
            if paren == '(':
                stack.append('(')
            if paren == ')':
                # pop the last '(' from the stack
                if not stack or stack.pop() != '(':
                    return False
        return not stack

    return 'Yes' if valid_parentheses(lst[0] + lst[1]) else 'No'
