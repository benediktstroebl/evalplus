
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
    for i in range(1, n+1):
        sum = 0
        for j in range(i):
            if j % 2 == 1:
                sum += lst[j]
        if sum > 0:
            return sum
    return 0
