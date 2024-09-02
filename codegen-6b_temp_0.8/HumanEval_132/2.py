
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
    # make a dictionary of all opening brackets and their positions
    # {'(':1, '[':2, '{':3}
    # {'(':1, '[':2, '{':3, ']':4, ')':5, '}':6}
    stack = []
    pos = {}
    for count, char in enumerate(string):
        if char == '[':
            pos[char] = count
        elif char == '(':
            stack.append(char)
        elif char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == '}':
            if len(stack) == 0:
                return False
            if stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif char == ']':
            if len(stack) == 0:
                return False
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
    