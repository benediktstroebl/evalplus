
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

    if not string or string == '[]':
        return True

    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        else:
            if len(stack) < 1:
                return False
            stack.pop()

    return True if len(stack) == 0 else False

