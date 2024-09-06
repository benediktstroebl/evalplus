
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
    if len(string) == 0:
        return True
    stack = []
    for item in string:
        if item == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return False
            else:
                stack.pop()
        else:
            stack.append(item)
    if len(stack) > 0:
        return False
    else:
        return True
