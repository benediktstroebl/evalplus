
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    # 1. Sum all the integers in the given list
    # 2. Return the sum of all odd integers in even positions

    total = sum(lst)
    odd_total = 0

    for i in range(len(lst)):
        if i%2 == 0 and lst[i]%2 != 0:
            odd_total += lst[i]

    return odd_total

