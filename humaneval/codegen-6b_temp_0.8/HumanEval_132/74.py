
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
    if string == '':
        return True
    
    if string[0] != '[':
        return False

    if string[-1] != ']':
        return False

    if len(string) == 1:
        return False
    
    stack = []
    for x in string:
        if x == '[' or x == ']':
            stack.append(x)

        if len(stack) == 0:
            return False
        
        if stack[-1] == ']' and x == '[':
            stack.pop()
        elif stack[-1] == '[' and x == ']':
            stack.pop()
        else:
            stack.append(x)

    if len(stack) != 0:
        return False

    return True
