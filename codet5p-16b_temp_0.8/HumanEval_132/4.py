
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

    for i in string:
        if i == '[':
            brackets_stack.append(i)
        elif i == ']':
            if len(brackets_stack) == 0:
                return False
            else:
                brackets_stack.pop()
    if brackets_stack:
        return False
    else:
        return True
