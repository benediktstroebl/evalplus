
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
    open_brackets_stack = []

    for char in string:
        if char == "]":
            if len(open_brackets_stack) > 0:
                open_brackets_stack.pop()
            else:
                return False
        else:
            open_brackets_stack.append(char)

    return len(open_brackets_stack) == 0
