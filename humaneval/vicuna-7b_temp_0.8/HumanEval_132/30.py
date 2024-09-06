
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
    open_brackets = 0
    for char in string:
        if char == '[':
            open_brackets += 1
        elif char == ']':
            open_brackets -= 1
        elif char == '[' and open_brackets > 0:
            stack.append(char)
            open_brackets -= 1
        elif char == ']' and open_brackets == 0:
            if len(stack) > 0:
                return True
        elif char == ']' and open_brackets == -1:
            if len(stack) == 0:
                return False
    return False
