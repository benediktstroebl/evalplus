
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
        open_count = 0
        for c in string:
            if c == '(':
                open_count += 1
            if c == ')':
                if open_count == 0:
                    return False
                open_count -= 1
        return open_count == 0

    string1 = lst[0] + lst[1]
    string2 = lst[1] + lst[0]
    return 'Yes' if is_balanced(string1) or is_balanced(string2) else 'No'
