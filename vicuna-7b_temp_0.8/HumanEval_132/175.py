
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
    for i, c in enumerate(string):
        if c == '[':
            stack.append(nest_level)
            nest_level += 1
        elif c == ']':
            if nest_level > 0:
                nest_level -= 1
                if stack[-1] == nest_level:
                    return True
            else:
                return False
        elif c == '\\':
            # skip escape characters
            i += 1
            continue

    return False