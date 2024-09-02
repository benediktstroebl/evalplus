
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
    # list = []
    # if len(q) == len(q[::-1]):
    #     list.append(True)
    # else:
    #     list.append(False)
    #
    # if sum(q) <= w:
    #     list.append(True)
    # else:
    #     list.append(False)
    # return list[0] and list[1]

    # return True if len(q) == len(q[::-1]) and sum(q) <= w else False
    # return True if q == q[::-1] and sum(q) <= w else False
    return q == q[::-1] and sum(q) <= w

    '''
    better solution:
    >>> from random import choice, randint
    >>> from pprint import pprint
    >>>
    >>> w = randint(0, 10)
    >>> l = [choice(range(10)) for _ in range(randint(0, 10))]
    >>>
    >>> pprint(will_it_
