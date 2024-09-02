
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
    def balanced(s):
        """
        Recursive function that counts the number of open
        and close parentheses, then recurses if the number
        of open is greater than the number of close.

        :param s: str
        :return: bool
        """
        c_open, c_close = 0, 0
        for ch in s:
            if ch == '(':
                c_open += 1
            elif ch == ')':
                c_open -= 1
                c_close += 1
            else:
                return False
        return c_open == c_close
    return balanced(lst[0]+lst[1])
