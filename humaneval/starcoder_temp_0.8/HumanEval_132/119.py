
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
    # If brackets are not even, return False
    if string.count('[]') % 2!= 0: return False

    # Check to see if string is composed of only brackets
    elif string == '[]' or string == '[][]' or string == '[][][]': return True

    # Create new string by removing the first two brackets at a time
    # Until no brackets are left
    while string!= '':
        # Check to see if string is composed of only brackets
        if string == '[]' or string == '[][]' or string == '[][][]': return True

        # Create new string by removing the first two brackets at a time
        else:
            new_string = string[2:]
            string = new_string

    # If no brackets are left, return False
    return False
