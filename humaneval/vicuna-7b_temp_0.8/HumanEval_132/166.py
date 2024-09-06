
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
    for i in range(len(string)):
        if i == 0:
            if string[i] == '[':
                stack.append(string[i])
        elif i == len(string) - 1:
            if stack:
                if string[i] == ']' and string[i-1] == stack[-1]:
                    stack.pop()
                elif string[i] == ']':
                    return True
            else:
                return False
        else:
            if stack and string[i] == '[':
                if i == len(string)-1:
                    stack.pop()
                stack.append(string[i])
            elif string[i] == ']':
                if stack:
                    if stack[-1] != string[i-1]:
                        stack.pop()
                    else:
                        stack.pop()
                else:
                    return False
    return False
