
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
    length = len(string)
    for i in range(length):
        if string[i] == '[':
            stack.append(i)
            while stack:
                j = stack.pop()
                if string[j] == '[':
                    stack.append(j+1)
                elif string[j] == ']':
                    break
                else:
                    break
        elif string[i] == ']':
            if len(stack) > 0:
                if stack[-1] != i-1:
                    return False
                stack.pop()
        else:
            if len(stack) == 0:
                return False
    return True
