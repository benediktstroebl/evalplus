
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
    a = '['
    b = ']'
    c = ''
    # For every item in string
    for i in string:
        # If the item is bracket
        if i == a:
            c = c + i
        # If item is a closing bracket
        elif i == b:
            # If the length of current stack is 0
            if len(c) == 0:
                # Return false
                return False
            # Else pop the stack
            c = c[:-1]
        # If item is neither bracket
        else:
            # Append to the stack
            c = c + i

    # Return true if stack is not empty
    return len(c) > 0
