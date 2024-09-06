
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
    current_depth = 0
    for c in string:
        if c == '[':
            stack.append(current_depth)
            current_depth += 1
        elif c == ']':
            if not stack:
                return False
            current_depth -= stack[-1]
            stack.pop()
    return current_depth > 0