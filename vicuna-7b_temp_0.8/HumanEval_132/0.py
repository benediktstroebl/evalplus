
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
    nest_level = 0
    current_char = string[0]
    for char in string[1:]:
        if char == current_char:
            nest_level += 1
        else:
            if nest_level > 0:
                stack.append(current_char)
            current_char = char
            nest_level = 1
    if current_char == ']':
        if stack:
            return True
        else:
            return False
    else:
        return False
