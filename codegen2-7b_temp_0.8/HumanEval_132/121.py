
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
    i=0
    a=[]
    n=0
    while i<len(string):
        if string[i]=='[':
            n+=1
            a.append(i)
            i+=1
        else:
            n-=1
            i+=1
        if n<0:
            return False
    if n==0:
        return True

