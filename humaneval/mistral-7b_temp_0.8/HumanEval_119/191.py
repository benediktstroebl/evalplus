
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

    # My solution:
    def match_parens(lst):
        if len(lst) < 1:
            return True
        elif len(lst) == 2:
            if lst[0] == lst[1]:
                return True
            else:
                return False
        else:
            if lst[0] == lst[1]:
                return match_parens(lst[2:])
            else:
                return False

    # Better solution:
    def match_parens(lst):
        for i in range(1, len(lst)):
            if lst[0] != lst[i] and lst[i] != lst[i-1]:
                return False
        return True

    # Another solution:
    def match_parens(lst):
        for i in range(len(lst)):
            if lst[i] == '(':
                stack.append(lst[i])
            elif lst[i] == ')':
                if len(stack) == 0:
                    return
