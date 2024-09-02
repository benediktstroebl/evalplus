
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
    if string[0] == ']': return False
    if string[-1] == '[': return False

    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if stack:
                stack.pop()
            else:
                stack.append(']')
    
    if stack: return True
    else: return False
