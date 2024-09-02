
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
    result = False
    if len(string) > 1:
        stack = []
        for i in range(len(string)):
            if string[i] == '[':
                stack.append(i)
            elif string[i] == ']':
                if len(stack) == 0:
                    return result
                else:
                    stack.pop()
        if len(stack) == 0:
            result = True
    return result
