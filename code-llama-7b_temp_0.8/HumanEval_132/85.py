
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

    nested_list = []

    for char in string:
        if char == '[':
            nested_list.append(char)
        elif char == ']':
            if nested_list and nested_list[-1] == '[':
                nested_list.pop()
            else:
                nested_list.append(char)
        else:
            continue

    if nested_list:
        return True
    else:
        return False
