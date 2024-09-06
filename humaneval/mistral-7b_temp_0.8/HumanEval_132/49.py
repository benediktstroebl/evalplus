
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

    # initialize a stack to store opening brackets
    stack = []

    # traverse through the string
    for char in string:
        # if the current character is an opening bracket
        if char == '[':
            stack.append(char)
        # if the current character is a closing bracket
        elif char == ']':
            # if the stack is empty
            if not stack:
                return False
            # if the closing bracket does not match the most recent opening bracket
            elif stack[-1] != '[':
                return False
            # if the closing bracket matches the most recent opening bracket, pop it from the stack
            else:
                stack.pop()
    # if the stack is not empty, there is a nested bracket sequence
    return len(stack) > 0
