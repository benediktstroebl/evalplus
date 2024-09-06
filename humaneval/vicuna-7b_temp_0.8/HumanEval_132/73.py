
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
    nesting = False
    for char in string:
        if char == '[':
            if stack:
                nesting = True
            else:
                stack.append(char)
        elif char == ']':
            if not nesting:
                return False
            else:
                nesting = False
                stack.pop()
    return not nesting
