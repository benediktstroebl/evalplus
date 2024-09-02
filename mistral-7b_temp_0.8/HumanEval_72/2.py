
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

    # Example of a balanced list:
    # [1, 2, 3]
    # [3, 2, 1]
    # [2, 1, 3]
    # [1, 3, 2]

    # Example of unbalanced list:
    # [1, 2]
    # [3, 2, 3]
    # [3, 2, 4]
    # [1, 3, 2, 1]

    # Example of a list that is not a palindromic list:
    # [1, 2, 3, 4]

    # Example of a list that is a palindromic list:
    # [1, 2, 3, 4, 3, 2, 1]
    if q == []:
        return True
    else:
        if q[-1] == q[0] and q[0] == q[1] and q[-1] == q[-2]:
            if sum(q) <= w:
                return True
            else:
