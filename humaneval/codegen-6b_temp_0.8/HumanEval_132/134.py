
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
    current_index = 0
    opening_brackets = 0
    closing_brackets = 0
    while current_index < len(string):
        if string[current_index] == '[':
            opening_brackets += 1
        elif string[current_index] == ']':
            closing_brackets += 1
        if opening_brackets == closing_brackets:
            return True
        current_index += 1
    return False

