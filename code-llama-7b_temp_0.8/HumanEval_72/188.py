
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if q==[]:
        return True
    elif len(q)%2==0:
        for i in range(0,len(q),2):
            if q[i]==q[len(q)-i-1]:
                if sum(q[i:len(q)-i-1])>w:
                    return False
            else:
                return False
        return True
    elif len(q)%2==1:
        for i in range(0,len(q)-1,2):
            if q[i]==q[len(q)-i-2]:
                if sum(q[i+1:len(q)-i-1])>w:
                    return False
            else:
                return False
        if q[len(q)-1]==q[0]:
            return True
        else:
            return False
