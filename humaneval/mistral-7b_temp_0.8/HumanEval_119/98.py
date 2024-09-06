
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


    # YOUR CODE HERE

    # Helper method to check if substring is good
    def is_good_substring(s):
        n = len(s)
        if n == 0:
            return True
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False

    # Helper method to check if string1 and string2 can be concatenated into a good string
    def can_concatenate(string1, string2):
        if len(string1) == 0 or len(string2) == 0:
            return False
        if string1[0] == string2[-1] and string1[0] == '(' and string2[-1] == ')':
            return is_good_substring(string1[1:] + string2[:-
