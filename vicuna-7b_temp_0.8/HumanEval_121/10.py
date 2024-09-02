
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0
    n = len(lst)
    odd_index = n%2+n//2
    odd_sum = 0
    for i in range(n):
        if i % 2 == 0:
            odd_sum += lst[i]
    return odd_sum
