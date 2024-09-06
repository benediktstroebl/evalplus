
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

    def is_balanced(q):
        #Make a copy of the list so that we can reverse it without changing the original list
        q2 = q.copy()
        q2.reverse()
        #If the two lists are equal, then it's balanced
        if q == q2:
            return True
        else:
            return False

    if is_balanced(q) and (sum(q) <= w):
        return True
    else:
        return False


    # ---- OR ----

    return q == q[::-1] and sum(q) <= w


