
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
    def bal(lst):
        s=0
        for a in lst:
            s+=a
        return s-int(s/2)*2 == 0

    def is_palindrom(lst):
        result=True
        for i in range(0,len(lst)/2):
            if lst[i] != lst[len(lst)-i-1]:
                result=False
        return result

    def is_sum(lst,w):
        s=0
        for a in lst:
            s+=a 
        return s <= w

    if is_palindrom(q) == False:
        return False
    else:
        return is_sum(q,w)

import pytest
