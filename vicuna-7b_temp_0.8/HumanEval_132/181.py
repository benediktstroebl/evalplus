
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
    nest_count = 0
    for i in range(len(string)-1):
        if string[i] == '[' and string[i+1] == '[':
            nest_count += 1
            if string[i+2] == ']':
                nest_count -= 1
        elif string[i] == ']':
            nest_count += 1
    return nest_count > 0
