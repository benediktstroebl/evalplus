
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
    nesting = []
    current = ''
    for char in string:
        if char == '[':
            if stack:
                nesting.append(current)
                stack.append(char)
            else:
                current = char
                stack.append(char)
        elif char == ']':
            if not stack:
                return False
            current = stack.pop()
            nesting.append(current)
            stack.pop()
        elif char == 'c':
            if stack:
                nesting.append(current)
                current = stack.pop()
            else:
                current = char
                stack.append(char)
        else:
            current += char
    if stack and not nesting:
        return False
    if nesting:
        return True
    return False
