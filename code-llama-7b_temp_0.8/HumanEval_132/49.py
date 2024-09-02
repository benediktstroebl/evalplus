
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

    # Initialize variables
    start_stack = []
    end_stack = []
    stack_length = 0
    temp_string = string

    # Check the length of the string
    if len(string) < 2:
        return False

    # Loop through the string
    for i, char in enumerate(string):
        # If it's a start bracket, add it to the start stack
        if char == '[':
            start_stack.append(char)
            stack_length += 1
            temp_string = temp_string[1:]
        # If it's a end bracket, pop a start bracket from the start stack
        elif char == ']':
            stack_length -= 1
            if stack_length > 0:
                start_stack.pop()
            else:
                start_stack = []
                return True

    return False
