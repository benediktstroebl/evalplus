
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
    
    for bracket in string:
        if bracket == '[' or bracket == ']':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) == 0 or stack[-1] == '[':
                return False
            else:
                stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
