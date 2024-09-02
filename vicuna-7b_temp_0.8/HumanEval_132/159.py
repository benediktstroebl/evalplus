
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
    start_index = 0
    for index in range(len(string)):
        if string[index] == '[' and index > start_index:
            nest_count += 1
            start_index = index
        elif string[index] == ']' and index > start_index:
            nest_count -= 1
            if nest_count < 0:
                return False
        elif nest_count == 0:
            return True
    return False

