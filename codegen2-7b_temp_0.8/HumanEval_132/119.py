
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
    
    flag=0
    arr = []
    string=string.strip()
    if(len(string)==0):
        return False
    for i in string:
        if(i=='['):
            flag+=1
            arr.append(i)
        elif(i==']'):
            if(flag==0):
                return False
            flag-=1
            arr.pop()
    if(flag!=0):
        return False
    return
