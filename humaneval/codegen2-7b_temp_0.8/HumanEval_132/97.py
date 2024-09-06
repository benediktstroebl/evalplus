
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
    brackets = ['[','{','(']
    stack = []
    
    for i in string:
        if i in brackets:
            stack.append(i)
            continue
        
        elif stack and i == brackets[brackets.index(stack[-1])]:
            stack.pop()
            continue
        else:
            return False
    
    return len(stack) == 0

