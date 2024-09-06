
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

    def is_good(text):
        cnt = 0
        for ch in text:
            if ch == '(':
                cnt += 1
            else:
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0

    def match(text1, text2):
        if len(text1) == 0:
            return is_good(text2)
        if len(text2) == 0:
            return is_good(text1)

        if text1[0] == '(' and text2[-1] == ')':
            return match(text1[1:], text2[:-1])
        if text1[-1] == ')' and text2[0] == '(':
            return match(text1[:-1], text2[1:])
        return False

    return 'Yes' if match(lst[0], lst[1]) else 'No'
