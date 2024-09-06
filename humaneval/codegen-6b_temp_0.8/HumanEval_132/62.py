
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
    
    # we use a stack to keep track of the opening brackets
    # the idea is to keep a counter of opening brackets
    # let's look at the string in reverse order
    # if it is a closing bracket,
    # add it to the stack, otherwise 
    # if the counter is > 0, although it is a closing bracket, 
    # we add a closing bracket to the stack because the residual string may be a valid subString of a nested string
    # checking the counter will determine if we have a valid subString of a nested string
    # this only gets checked for the closing bracket, but not for the opening bracket
    # as we add to the stack, if the counter is > 0, we know we have a nested string
    # if we reach the end of the string, we return True

    # Time - O(n)
    # Space - O(n)
    
    # check if the string is empty
    if len(string) == 0:
        return True

    opening_bracket = {'(':1, '[':2, '{':3}
    closing_bracket = {')':1, ']':2, '}':3}
    stack = []

    for char in reversed(string):
        if char in closing_bracket:
            stack.append(char)
        elif char in opening_bracket:
            if len(stack) == 0 or opening_bracket.get(char) != closing_bracket.get(stack.pop()):
                return False
        else:
            return False
    
    return len(stack) == 0
