
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
    if len(q)<1:
        return False
    if len(q)==1:
        return True
    if q[0]==q[len(q)-1]:
        for i in range(1,len(q)):
            if q[i]>q[len(q)-i-1]:
                return False
        return True
    return False

q = [1,2,3,4,5]
print(will_it_fly(q, 5))

q = ['a','b','c','d','e','f','g','h']
print(will_it_fly(q, 1))

q = [3,2,3]
print(will_it_fly(q, 9))

q = [3]
print(will_it_fly(q, 5))

q = [100,101,102,103,104,105]
print(will_it_fly(q, 11))
