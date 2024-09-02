
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
    for i in range(len(string)):
        if string[i] == '[' and stack:
            if stack[-1] != ']':
                return False
        elif string[i] == ']' and not stack:
            if stack[-1] == '[':
                return False
        elif string[i] == ']':
            stack.pop()
        elif string[i] == '[':
            stack.append(i)
        else:
            stack.pop()
    return not stack
