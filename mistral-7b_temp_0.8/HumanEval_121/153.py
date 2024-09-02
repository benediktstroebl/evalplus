
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if lst is None:
        return None
    ans = 0
    for i, j in enumerate(lst):
        if i % 2 == 0 and j % 2 != 0:
            ans += j
    return ans
