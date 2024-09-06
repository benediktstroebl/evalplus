
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

    brackets_stack = []

    for char in string:
        if char == '[':
            brackets_stack.append(']')
        if char == ']':
            if not brackets_stack:
                return False
            elif brackets_stack.pop()!= char:
                return False

    return not brackets_stack
