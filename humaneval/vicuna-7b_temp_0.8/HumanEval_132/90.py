
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
    string = string.upper()
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack:
                if stack[-1] == '[':
                    return True
                elif stack[-1] == ']':
                    return False
                else:
                    stack.pop()
        elif char == '(':
            if not stack or stack[-1] != '[':
                return False
            stack.append('[')
        elif char == ')':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return False