
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
    
    l = len(string)
    for first in range(l):
        for second in range(first+1,l):
            if string[first] == '[' and string[second] == ']' and (first+2 < second < l - 1):
                if (string[first+1] == '[' and string[second-1]==']') or (string[first+2] == '[' and string[second-2] == ']') or (string[first-1] == '[' and string[second+1]==']') or (string[first-2] == '[' and string[second+2]==']'):
                    return True
    return False
    