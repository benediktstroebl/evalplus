
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''


    s = string
    def is_valid(s):
        stack = []
        for char in s:
            if char == '[':
                stack.append(char)
            elif char == ']':
                if stack:
                    last_open_bracket = stack.pop()
                    if last_open_bracket != '[':
                        return False
                else:
                    return False
        return True

    for i in range(len(s)):
        if is_valid(s[i:]):
            return True
    return False




    '''
    s = '['
    stack = []
    for i in range(len(s)):
        if s[i] == '[':
            stack.append(s[i])
        if s[i] == ']':
            if stack:
                last_open_bracket = stack.pop()
                if last_open_bracket != '[':
                    return False
            else:
                return False
    if len(stack) > 0
