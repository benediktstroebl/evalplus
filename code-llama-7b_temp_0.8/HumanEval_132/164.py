
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
    # get all the indexes
    inds = [i for i, char in enumerate(string) if char == "[" or char == "]"]

    # iterate over each group and check if it is nested
    for i in range(len(inds)-2):
        if (string[inds[i]] == "[" and string[inds[i+1]] == "["):
            return True
    
    return False



