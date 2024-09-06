
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
    # Use a stack to keep track of the brackets
    stack = []
    for i in range(len(string)):
        if string[i] == '[' and stack != []:
            # If a bracket is found, it is a nested bracket if it is nested inside another bracket
            if stack[-1] == ']':
                if stack[-2] == '[':
                    return True
            stack.pop()  # Remove the most recent bracket from the stack
        elif string[i] == ']':
            stack.append(string[i])  # Add the most recent bracket to the stack
    return False  # If no bracket is found on the stack, return False