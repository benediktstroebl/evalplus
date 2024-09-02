
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
    # Remember to remove the "Notes:" and "Examples:" from below before submitting!

    if len(string)==0:
        return False
    
    left_bracket_count, right_bracket_count = 0, 0
    
    for i in range(len(string)):
        if string[i] == '[':
            left_bracket_count += 1
        elif string[i] == ']':
            if left_bracket_count > 0:
                left_bracket_count -= 1
                right_bracket_count += 1
            else:
                return False

    return left_bracket_count == right_bracket_count
    
