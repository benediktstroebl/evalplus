
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
    def match_parenthesis(string):
        opened_brackets = []
        for c in string:
            if c == "(":
                opened_brackets.append(c)
            elif c == ")":
                if len(opened_brackets) == 0:
                    return False
                else:
                    opened_brackets.pop()
        if len(opened_brackets) == 0:
            return True
        else:
            return False

    return 'Yes' if match_parenthesis(lst[0]) and match_parenthesis(lst[1]) else 'No'
