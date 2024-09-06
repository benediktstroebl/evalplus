
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
    nested = False
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack:
                if stack[-1] == '[':
                    nested = True
                else:
                    nested = False
                stack.pop()
        elif char == 'n':
            nested = not nested
        elif char == 'o':
            nested = not nested
        elif char == 'd':
            nested = not nested
        elif char == 'e':
            nested = not nested
    return nested
