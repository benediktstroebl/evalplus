
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
    openers = ['(', '[', '{']
    closers = [')', ']', '}']
    stack = []
    for char in string:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if len(stack) == 0:
                return False
            if closers.index(char) != openers.index(stack.pop()):
                return False
    return len(stack) == 0

