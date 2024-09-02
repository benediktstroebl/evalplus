
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
    # check the length of the string
    if len(string) != 1:
        return False
    
    # check if the string is valid by checking if it starts and ends with a bracket
    if string[0] != '[' or string[-1] != ']':
        return False
    
    # check if there is a nested bracket
    for i in range(1, len(string) - 1):
        if string[i] == '[' and string[i+1] == '[':
            nested_indices = [i+2, i+3, i+4]
            for j in nested_indices:
                if string[j] == ']':
                    if string[j-1] == '[':
                        # there is a nested bracket
                        return True
    return False
