
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    total = 0
    for i in range(n-1):
        if lst[i] % 2 == 0:
            total += lst[i]
            lst[i],lst[i+1] = lst[i+1],lst[i]
    total += lst[n-1]
    return total
