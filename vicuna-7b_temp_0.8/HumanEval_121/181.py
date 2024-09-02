
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    odd_sum = 0
    for i in range(n):
        odd_sum += lst[i] if i % 2 != 0 else 0
    return odd_sum

