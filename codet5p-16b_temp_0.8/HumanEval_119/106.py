
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

    def balance(lst):
        '''
        Return True if the list contains only open parentheses, False otherwise
        '''
        s = []
        for i in range(len(lst)):
            if lst[i] == '(' and len(s) > 0 and s[-1] == ')':
                s.pop()
            else:
                s.append(lst[i])
        return len(s) == 0

    def permutations(lst):
        '''
        Return a list of all possible concatenations of the given list of items.
        '''
        perms = []
        if len(lst) == 1:
            perms.append(lst)
        else:
            for i in range(len(lst)):
                temp = lst[i]
                sublst = lst[:i] + lst[i+1:]
                if len(sublst) == 0:
                    perms.append([temp])
                else:
                    for perm in permutations(sublst):
                        perms.append
