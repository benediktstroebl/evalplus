
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    left = 0
    right = max(lst)
    ans = 0
    while left <= right:
        if lst[left] % 2 == 0:
            left += 1
        else:
            ans += lst[left]
            left += 1
    return ans
