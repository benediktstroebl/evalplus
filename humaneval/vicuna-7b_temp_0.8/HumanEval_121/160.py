
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
    i = 0
    while i < n/2:
        j = i + 1
        while j < n:
            if j % 2 == 1:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
    return lst[n]
