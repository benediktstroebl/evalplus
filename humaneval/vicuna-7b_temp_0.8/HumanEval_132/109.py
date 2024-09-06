
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
    last_index = 0
    for i in range(len(string)):
        if string[i:i+2] == '[]':
            stack.append(string[last_index:i])
            last_index = i+2
        elif string[i:i+2] == ']':
            if len(stack) > 0:
                if stack[-1] == '[]':
                    return True
                else:
                    stack.pop()
            else:
                return False
        else:
            last_index = i+1
    if len(stack) > 0:
        if stack[-1] == '[]':
            return True
        else:
            return False
    else:
        return False
