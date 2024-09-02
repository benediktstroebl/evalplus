
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
    bracket_map = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    for bracket in string:
        if bracket in bracket_map:
            stack.append(bracket_map[bracket])
        elif stack and bracket == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack
