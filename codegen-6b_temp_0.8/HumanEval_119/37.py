
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
    def is_balanced_and_balanced_partition(string):
        if(len(string) % 2 == 1):
            return False
        stack = []
        for s in string:
            if s == '(':
                stack.append(s)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
        return len(stack) == 0

    n = len(lst)
    s = set()
    for i in range(n):
        for j in range(i+1, n):
            str_i = lst[i]
            str_j = lst[j]
            if is_balanced_and_balanced_partition(str_i) and is_balanced_and_balanced_partition(str_j):
                s.add(str_i + str_j)
    return 'Yes' if len(s) > 0 else 'No'

