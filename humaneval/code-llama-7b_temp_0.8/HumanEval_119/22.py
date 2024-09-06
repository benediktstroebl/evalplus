
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
    # check if a string is good
    def is_good(s):
        # initialize the stack
        stack = []
        # for each character in the string
        for c in s:
            # if the character is '('
            if c == '(':
                # append it to the stack
                stack.append('(')
            # if the character is ')'
            if c == ')':
                # if there is something in the stack, and the last element
                # in the stack is '('
                if stack and stack[-1] == '(':
                    # pop the element from the stack
                    stack.pop()
                # otherwise
                else:
                    # append the character to the stack
                    stack.append(')')
        # if there are elements in the stack
        if stack:
            # return false
            return False
        # otherwise
        else:
            # return true
            return True

    # concatenate two strings in some order
    def combine(s1, s2):
        # for each character in the first string
        for c in s1:
            # append the character to the second string
            s2.append(c)
        # return the second string
        return s2
    # concatenate two strings in some order
    def combine(s1, s2):
        # for each character in the second string
        for c in s2:
            # append the character to the first string
            s1.append(c)
        # return the first string
        return s1

    # initialize the result variable
    result = []
    # for each string in the list
    for s in lst:
        # if the string is good
        if is_good(s):
            # append the string to the result variable
            result.append(s)
    # if there are two strings in the result variable
    if len(result) == 2:
        # concatenate the two strings
        res = combine(result[0], result[1])
        # if the result string is good
        if is_good(res):
            # return yes
            return 'Yes'
        # otherwise
        else:
            # return no
            return 'No
