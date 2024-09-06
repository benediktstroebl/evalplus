
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
    stack = []
    last_close_pos = -1
    for char in string:
        if char == '[':
            if stack:
                if last_close_pos == -1 or stack[-1] != ']':
                    return False
            stack.append('[')
            last_close_pos = len(string) - 1
        elif char == ']':
            if stack:
                if last_close_pos == -1 or stack[-1] != '[':
                    return False
                stack.pop()
                last_close_pos = -1
        elif char == ']':
            if stack:
                if last_close_pos == -1 or stack[-1] != '[':
                    return False
                stack.pop()
                last_close_pos = -1
        elif char == ']':
            return True
    return False