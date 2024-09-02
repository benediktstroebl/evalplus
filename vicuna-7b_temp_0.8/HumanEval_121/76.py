
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
    for i in range(n/2):
        if lst[i]%2 == 0:
            lst[i],lst[n-i-1] = lst[n-i-1],lst[i]
            odd_sum = 0
            for j in range(i):
                odd_sum += lst[j]
            return odd_sum
    return 0
