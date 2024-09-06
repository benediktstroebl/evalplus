
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

    left_brackets_count = 0
    right_brackets_count = 0
    for i in range(len(string)):
        if string[i] == '[':
            left_brackets_count += 1
            if left_brackets_count == 1:
                right_brackets_count = 0
        elif string[i] == ']':
            right_brackets_count += 1
            if right_brackets_count == 1:
                left_brackets_count = 0
            if left_brackets_count == 0:
                return True
            
    return False

