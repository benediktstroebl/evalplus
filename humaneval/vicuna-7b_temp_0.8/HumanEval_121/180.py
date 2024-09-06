
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # no need to check if the list is empty, because we are not going to use it in any case
    if not lst:
        return 0

    return sum(lst[i:i+2] for i in range(0, len(lst), 2))
