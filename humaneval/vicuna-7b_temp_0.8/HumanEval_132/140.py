
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
    visited = set()
    for char in string:
        if char == '[':
            stack.append(char)
            visited.add(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            top_char = stack.pop()
            visited.remove(top_char)
            if top_char == '[':
                stack.append(top_char)
                visited.add(top_char)
            else:
                return True
    return False
