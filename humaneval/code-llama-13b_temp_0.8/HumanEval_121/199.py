
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if len(lst) == 1:
        if lst[0] % 2 == 0:
            return lst[0]
        else:
            return 0
    else:
        if lst[1] % 2 != 0:
            return lst[1] + solution(lst[2:])
        else:
            return solution(lst[2:])
