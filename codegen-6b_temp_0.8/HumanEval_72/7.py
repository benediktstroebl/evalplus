
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
    # q = [1, 2, 3, 2, 1]
    # sum_of_q = sum(q)
    # max_weight = 9
    # while sum_of_q < max_weight:
    #     if is_palindrome(q) is True:
    #         if sum_of_q < max_weight:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    #     q.append(q.pop(0))
    #     sum_of_q = sum(q)
    # return True

    ## Code from https://github.com/nicoftrunk/will_it_fly
    q = [1, 2, 3, 2, 1]
    sum_of_q = sum(q)
    max_weight = 9
    if sum_of_q <= max_weight and is_palindrome(q) is True:
        return True
    else:
        return False


