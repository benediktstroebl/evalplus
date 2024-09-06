
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

    def find_all(s, ch):
        result = []
        index = 0
        while index < len(s):
            index = s.find(ch, index)
            if index == -1:
                return result
            result.append(index)
            index += 1
        return result
    
    def is_valid(s, lst):
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack == []:
                    return 'No'
                stack.pop()
        if stack == []:
            return 'Yes'
        return 'No'
    
    def rec(lst, start, end):
        if start == end:
            return is_valid(lst[start], lst)
        for i in range(start, end):
            temp = lst[start:end]
            if is_valid(temp[0], lst) == 'Yes':
                if rec(lst, start+1, i) == 'Yes':
                    return 'Yes'
                el
