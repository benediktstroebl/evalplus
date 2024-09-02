
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

    bracket_stack = []
    bracket_map = {'{': '}', '[': ']', '(': ')'}
    for char in string:
        if char in bracket_map:
            bracket_stack.append(char)
        elif char in bracket_map.values():
            if not bracket_stack:
                return True
            last = bracket_stack.pop()
            if bracket_map[last]!= char:
                return True
        else:
            return False

    if bracket_stack:
        return True
    return False


