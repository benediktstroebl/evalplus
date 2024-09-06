
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
    # loop through the string
    stack = []
    for x in string:
        # check if its opening
        if x == '[':
            stack.append(x)
        # if it is closing, check if there is something to open
        elif x == ']':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    # check if there are still something in the stack
    if len(stack) > 0:
        return True
    else:
        return False



