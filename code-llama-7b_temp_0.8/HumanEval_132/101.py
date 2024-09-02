
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
    stack, check = [], []
    if len(string)%2 != 0: return False
    
    for s in string:
        if s == '[':
            stack.append('[')
        elif s == ']':
            if len(stack) != 0:
                stack.pop()
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                    if len(stack) == 0:
                        return True
            else:
                return False
    return len(stack) == 0
