
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
    for bracket in list(string):
        if bracket == '}' and len(stack) > 0 and stack.pop() == '{':
            continue
        if bracket == ']' and len(stack) > 0 and stack.pop() == '[':
            continue
        if len(stack) == 0:
            stack.append(bracket)
        else:
            stack.append(bracket)

    return len(stack) == 0

