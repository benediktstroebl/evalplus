
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

    # Try to find nested brackets
    for i in range(len(string)):
        if string[i:i+2] == '[[]':
            # Check if nested brackets exist
            nested = True
            for j in range(i+2, len(string)):
                if string[j:j+2] == '[]' and string[j+1:j+3] == '[]':
                    nested = False
                    break
            if nested:
                return True
    return False
