
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
    nesting_level = 0
    for char in string:
        if char == '[':
            stack.append(nesting_level)
            nesting_level += 1
        elif char == ']':
            if stack:
                nesting_level = stack.pop()
            else:
                return False
        elif char == '[' or char == ']':
            return False
    return True
