
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
    if string == '[]':
        return False
    
    pairs = {'[':']'}
    stack = []
    for i in string:
        if i in pairs:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if pairs[stack[-1]] == i:
                stack.pop()
            else:
                return False
    return len(stack) == 0


