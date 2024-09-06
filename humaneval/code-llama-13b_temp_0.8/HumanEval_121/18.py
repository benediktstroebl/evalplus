
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0

    final_sum = 0
    for index, value in enumerate(lst):
        if index % 2 == 0 and value % 2 != 0:
            final_sum += value

    return final_sum

