
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
    elif n % 2 == 0:
        return lst[0]
    else:
        for i in range(1, n):
            if lst[i] % 2 == 1:
                lst[i], lst[i-1] = lst[i-1], lst[i]
        return lst[0] + solution(lst[1:])
