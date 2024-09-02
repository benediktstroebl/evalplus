
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
    if len(string)==0:
        return False
    elif string[0] == ']':
        return False
    elif string[-1] == '[':
        return False
    else:
        i=0
        while i < len(string):
            if string[i] == '[' and string[i+1] == ']':
                i +=2
            else:
                i +=1
        if i == len(string):
            return True
        else:
            return False






