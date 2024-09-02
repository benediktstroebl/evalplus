
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
        if string[i] == '[':
            stack.append(string[i])
        elif string[i] == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    if not stack:
        return True
    else:
        return False
