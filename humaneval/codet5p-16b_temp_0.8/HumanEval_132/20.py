
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

    if not string: return False
    
    stack = []
    for i, char in enumerate(string):
        if char == '[':
            stack.append((i, char))
        elif char == ']':
            if stack:
                last = stack.pop()
                if last[1] == '[' and i - last[0] == 1:
                    return True
            else:
                return False
    return False if stack else True
