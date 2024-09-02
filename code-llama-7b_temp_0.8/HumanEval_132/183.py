
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
    # Returns true if any valid sequence is found in the string
    # Returns false if no valid sequence is found in the string

    # Set up variables
    bracket_dict = {
        ']' : '[',
        '}' : '{',
        ')' : '(',
    }

    # set up open_bracket_stack
    open_bracket_stack = []

    # check the string for all valid brackets
    for char in string:
        if char in bracket_dict.values():
            # Add opening brackets to the stack
            open_bracket_stack.append(char)
        elif char in bracket_dict.keys():
            # Check if the current char matches the last open bracket in the stack
            if open_bracket_stack != [] and bracket_dict[char] == open_bracket_stack[-1]:
                # Remove the last bracket from the stack if they match
                open_bracket_stack.pop()
            else:
                # Otherwise, there is an invalid bracket
                return False
    
    # If the string has not returned false by now, return true
    if len(open_bracket_stack) == 0:
        return True
    else:
        return False
