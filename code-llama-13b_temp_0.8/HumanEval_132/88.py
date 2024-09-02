
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
    a=[]
    for i in string:
        if i in ['[','['] and len(a)>0:
            a.append(i)
        elif i in [']']:
            if len(a)==0 or a[-1] ==']':
                return False
            else:
                a.pop()
    if len(a)==0:
        return False
    else:
        return True


