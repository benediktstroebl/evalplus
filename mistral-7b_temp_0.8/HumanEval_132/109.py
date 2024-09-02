
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
    n = len(string)
    stack = []
    for i in range(n):
        if stack and string[i] == '[':
            stack.append(string[i])
        elif stack and string[i] == ']':
            stack.pop()
        elif string[i] == '[':
            stack.append(string[i])
    if stack:
        return True
    else:
        return False
