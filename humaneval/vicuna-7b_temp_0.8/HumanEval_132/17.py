
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
    string = '[]' if string == '[]' else string

    for char in string:
        if char == '[' or char == ']':
            stack.append(char)
        elif char == ']':
            if stack:
                if stack[-1] == '[' and stack[-2] != ']':
                    visited.add(stack.pop())
                    stack.append(stack[-2])
                elif stack[-1] == ']' and stack[-2] == '[' and char not in visited:
                    visited.add(stack.pop())
                    stack.append(char)
            elif not stack:
                return False

    return True