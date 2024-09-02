
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
    nested = False
    for char in string:
        if char == '[':
            stack.append(char)
            nested = True
        elif char == ']':
            if nested:
                nested = False
                stack.pop()
                if stack == []:
                    return True
            else:
                return False
        elif char == '|':
            stack.append('[']*int(stack.pop(0))
    return False