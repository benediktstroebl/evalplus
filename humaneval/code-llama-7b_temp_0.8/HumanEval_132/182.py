
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
    l=list(string)
    if l==[]:
        return False
    
    for i in range(len(l)):
        if l[i]=="]":
            return False
        
        if l[i] in ('[',']'):
            if i<len(l)-1:
                if l[i+1] not in ('[',']'):
                    return False
    for i in range(len(l)):
        if l[i] == "[":
            return True
    
    return False

