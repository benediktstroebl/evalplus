
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
    # 1st solution: recursive solution
    def match_helper(lst, str1, str2):
        if not lst:
            if str2.count('(') == str2.count(')'):
                return 'Yes'
            else:
                return 'No'

        if lst[0] == ')':
            return match_helper(lst[1:], str1 + '))', str2)
        else:
            return match_helper(lst[1:], str1 + '(', str2 + lst[0])

    return match_helper(lst, '', '')

    # 2nd solution: iterative solution
    # def match_parens(lst):
    #     if not lst:
    #         return 'No'
    #     str1 = ''
    #     str2 = ''
    #     stack = []
    #     for i in lst:
    #         if i == ')':
    #             if not stack:
    #                 return 'No'
    #             elif stack.pop() == '(':
    #                 str1 += '))'
    #                 str2 += i
    #             else:
    #                 return 'No'
    #         else:
    #             str1 += '('
    #             str2 += i
    #             stack.append('(')
    #     if stack:
    #         return 'No'
    #     if str2.count('(') == str2.count(')'):
    #         return 'Yes'
    #     else:
    #         return 'No'
