
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
    # #0
    # if q is None:
    #     return False
    # if len(q) == 0:
    #     return False
    # if q is []:
    #     return False
    # if len(q) % 2 == 1:
    #     return False
    # if sum(q) <= w:
    #     return False
    # if len(q) == 1:
    #     if q[0] <= w:
    #         return True
    #     return False
    # max_weight = w - sum(q[:len(q)//2])
    # if max_weight < 0:
    #     return False
    # if max_weight <= q[len(q)//2]:
    #     return True
    # return False

    #1
    if not q or len(q) == 1:
        return False
    if sum(q) > w:
        return False
    if len(q) == len(q) // 2 + 1:
        return True
    return False

    '''
    test 1
    print(will_it_fly([1, 2], 5))
    # False
    
    test 2
    print(will_it_fly([3, 2, 3], 1))
    # False
    
    test 3
    print(will_it_fly([3, 2, 3], 9))
    # True
    
    test 4
    print(will_it_fly([3, 2, 3], 8))
    # True
    '''

    #? What's the time complexity?
    # if q is None or len(q) == 0:
    #     return False
    # if len(q) % 2 == 1:
    #     return False
    # max_weight = w - sum(q[:len(q)//2])
    # if max_weight < 0:
    #     return False
    # if len(q) == 1:
    #     if q[0] <= w:
    #         return True
    #     return False
    # if q[len(q)//2] <= max_weight:
    #     return True
    # return False