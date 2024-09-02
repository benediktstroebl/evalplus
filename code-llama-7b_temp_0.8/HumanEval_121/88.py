
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # ------------------------------------------------------------------
    # 1. find odd element in even position
    # 2.  sum all the odd element in even position
    # ------------------------------------------------------------------
    sum_odd = 0
    for i in range(len(lst)):
        # if i % 2 == 0:
        if (i + 1) % 2 == 0:
            if lst[i] % 2 == 1:
                sum_odd += lst[i]
    return sum_odd

    # return sum([num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 1])
    # return sum([num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 1])
    # return sum([num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 1])

    # ------------------------------------------------------------------
    # How to find odd element in even position
    # odd = [num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 1]
    # return sum(odd)
    # ------------------------------------------------------------------

