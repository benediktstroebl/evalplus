
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    left = 0
    right = max(lst)
    result = 0
    while right - left > 1:
        mid = (left + right) // 2
        if mid * 2 < len(lst) and lst[mid] % 2 == 0:
            left = mid + 1
            result += lst[mid]
        else:
            right = mid
            result += lst[mid]
    return result
