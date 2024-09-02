
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
    # Use a stack to keep track of open brackets.
    # If the stack is empty, we have reached the end of the string.
    # If the last element of the stack is ']', it means we have a nested bracket.
    # If the last element of the stack is '(', it means we have a nested bracket, but it is not valid.
    stack = []
    for char in string:
        if char == ']':
            if stack:
                # If the last element of the stack is '[', it means we have a nested bracket.
                # This means the bracket is not valid.
                return False
        elif char == '(':
            if not stack:
                # If the first element of the stack is '(', it means we have a nested bracket.
                # This means the bracket is not valid.
                return False
            stack.pop()
        else:
            stack.append(char)
    return True