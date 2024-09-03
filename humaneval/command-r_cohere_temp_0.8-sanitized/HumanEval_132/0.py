def is_nested(s):
    '''
    Checks if a string containing only brackets has a nested bracket sequence.
    '''
    stack = []
    for i in s:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) > 1 and stack[-2] == '[':
                stack.pop()
                stack.pop()
            else:
                return False
        else:
            raise Exception('Invalid input string')
            
    return len(stack) > 0