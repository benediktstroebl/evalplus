
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
    nest_level = 0
    for char in string:
        if char == '[':
            if stack:
                if nest_level == 0:
                    return False
                else:
                    nest_level -= 1
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            else:
                char = stack.pop()
                nest_level += 1
    return True