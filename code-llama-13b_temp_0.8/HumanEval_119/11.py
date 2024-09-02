
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
    # my_list = ['()(', ')']
    # my_list = [')', ')']
    # my_list = ['(', ')']
    # my_list = ['()(', ')']
    # my_list = ['(((', '))', '())']
    # my_list = ['(((', '())', '))']
    # my_list = ['()(', '(()', '))']

    # O(n) time | O(1) space
    def helper(lst, start, end):
        stack = []
        for i in range(start, end):
            if lst[i] == '(':
                stack.append(lst[i])
            else:
                if not len(stack):
                    return False
                stack.pop()
        return not len(stack)

    end = len(lst)
    for start in range(end):
        if helper(lst, 0, end):
            return 'Yes'
        lst.append(lst.pop(0))
    return 'No'
