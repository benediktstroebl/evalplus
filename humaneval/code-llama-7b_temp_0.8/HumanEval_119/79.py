
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
    # pylint: disable=R0913
    def check_balanced(lst):
        """Check if a list is balanced or not."""
        stack = []
        for paren in lst:
            if paren == '(':
                stack.append(paren)
            elif len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
        return len(stack) == 0

    lst1 = lst[0]
    lst2 = lst[1]

    str1 = lst1 + lst2
    str2 = lst2 + lst1

    return 'Yes' if check_balanced(str1) or check_balanced(str2) else 'No'
