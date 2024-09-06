
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
    for char in string:
        if char == '[':
            if len(stack) > 0:
                if stack[-1] != ']':
                    return False
                stack.pop()
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
        elif char == ']':
            if len(stack) == 0:
                return False
            elif stack[-1] != ']':
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack