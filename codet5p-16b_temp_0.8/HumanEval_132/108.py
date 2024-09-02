
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

    bracket_stack = []
    for i in string:
        if i == '[':
            bracket_stack.append(i)
        elif i == ']' and len(bracket_stack) > 0 and bracket_stack[-1] == '[':
            bracket_stack.pop()
        elif i == ']' and len(bracket_stack) > 0 and bracket_stack[-1] == ']':
            return False

    if len(bracket_stack) == 0:
        return True
    else:
        return False
