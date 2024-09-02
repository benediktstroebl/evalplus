
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
    for i, char in enumerate(string):
        if char == '[':
            stack.append(i)
        elif char == ']':
            if len(stack) == 0:
                return True
            stack.pop()
    return False if len(stack)!= 0 else True
