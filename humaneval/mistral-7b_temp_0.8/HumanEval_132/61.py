
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
    result = False
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        if char == ']':
            stack.pop()
            if len(stack) == 0:
                break

    if len(stack) == 0:
        result = True
    return result
