
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
    is_nested_bool = False
    for i, char in enumerate(string):
        if char == '[':
            is_nested_bool = True
            break
        elif char == ']':
            is_nested_bool = False
        else:
            continue
            
    if is_nested_bool:
        return True
    else:
        return False
            




