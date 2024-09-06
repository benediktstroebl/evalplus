
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

    brackets_stack = []
    for c in string:
        if c == '[':
            brackets_stack.append(c)
        elif c == ']':
            if len(brackets_stack) == 0:
                return False
            else:
                brackets_stack.pop()
    if len(brackets_stack) > 0:
        return False
    else:
        return True
