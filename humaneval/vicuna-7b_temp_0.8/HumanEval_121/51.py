
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    low = 0
    high = len(lst) - 1
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] % 2 == 0:
            low = mid + 1
        else:
            result += lst[mid]
            low = mid + 1
    return result
