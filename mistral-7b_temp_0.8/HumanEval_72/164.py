
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
    q = list(q)
    if sum(q) <= w:
        return len(q) == len(q[::-1])
    return False


    # my solution

    # if len(q) % 2 == 0:
    #     first_half = q[0:len(q)//2]
    #     second_half = q[len(q)//2:]

    #     if sum(first_half) + sum(second_half) <= w and first_half == second_half[::-1]:
    #         return True
    #     else:
    #         return False
    # else:
    #     first_half = q[0:len(q)//2]
    #     second_half = q[len(q)//2 + 1:]

    #     if sum(first_half) + sum(second_half) <= w and first_half == second_half[::-1]:
    #         return True
    #     else:
    #         return False


    # solution

    #
