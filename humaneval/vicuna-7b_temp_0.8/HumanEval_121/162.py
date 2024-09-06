
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    left, right = 1, 1
    for num in lst:
        if (num % 2) == 0:
            continue
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right += 1
    return left

