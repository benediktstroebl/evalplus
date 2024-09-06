
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
    for symbol in string:
        if symbol == '[':
            stack.append(symbol)
            if len(stack) > 0:
                if stack[-1] == ']':
                    stack.pop()
                elif stack[-1] == '[':
                    stack.pop()
                    stack[-1] = '['
        elif symbol == ']':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return not stack
