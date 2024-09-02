
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
    if len(string)==1:
        return False
    
    pos=1
    for i in range(len(string)-1):
        if string[pos]==']' and string[pos-1]==']':
            return True
        elif string[pos]=='[' and string[pos-1]==']':
            pos+=1
            while pos<len(string)-1:
                if string[pos]==']' and string[pos+1]=='[':
                    return True
                pos+=1
        pos+=1
    
    return False
