
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
    def will_it_fly_helper(q,w):
        if not q:
            return 0
        if len(q)==1:
            return q[0]
        if len(q)==2:
            return max(q[0],q[1])
        mid=len(q)/2
        left,right=(q[:mid],q[mid:])
        if sum(left)<=w:
            return will_it_fly_helper(left,w)
        elif sum(right)<=w:
            return will_it_fly_helper(right,w)
        else:
            return False
    return will_it_fly_helper(q,w)
assert will_it_fly([3,2,3], 9)==True
assert will_it_fly([3,2,3], 5)==False
assert will_it_fly([1,2], 5)==False
assert will_it_fly([1,2], 1)==True
assert will_it_fly([1,2], 9)==False
assert will_it_fly([1,2,3], 5)==False
assert will_it_fly([1], 5)==True


