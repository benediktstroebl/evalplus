
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

    #Equal length lists are a palindrome
    if len(q) == 1:
        return True
    elif len(q) == 2:
        # Equal length and the elements are equal
        if q[0] == q[1]:
            return True
    else:
        # Number of elements that are less than the last one
        x = 0
        # Number of elements that are greater than the last one
        y = 0
        for i in range(len(q)):
            if q[i] < q[-1]:
                x += 1
            else:
                y += 1
        if x > y:
            return False
        elif y > x:
            return False
        elif x == y:
            if q[0] == q[-1]:
                return True
            else:
                return False
    return False


