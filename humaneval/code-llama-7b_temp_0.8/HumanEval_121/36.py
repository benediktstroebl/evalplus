
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i)
    result_sum = 0
    for j in result:
        if j % 2 != 0:
            result_sum += j
    return result_sum
