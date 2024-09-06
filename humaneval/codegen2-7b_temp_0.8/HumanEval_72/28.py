
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
    n = len(q)
    s = sum(q)
    if n == 0 or n == 1 or n == 2:
        return True
    if (n == 3 and s > w):
        return False
    if (n % 2 == 0 and s > w/2):
        return False
    if (n % 2 == 1 and s > w/2):
        return False
    return will_it_fly(q[1:n/2], w-s) and will_it_fly(q[n/2+1:], w-s)








