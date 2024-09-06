
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    if n < 2:
        return 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[j] % 2 == 0:
                lst[i], lst[j] = lst[j], lst[i]
                if j-1 >= 0:
                    solution(lst)
    return lst[n-2] + lst[n-1]