
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
    nest=[]
    for i in range(len(string)-1):
        if string[i]=='[':
            nest.append(i)
        if string[i]==']':
            if nest:
                nest.pop()
            else:
                return False
    if nest:
        return is_nested(string[:nest[0]+1]+string[nest[0]+1:])
    else:
        return
