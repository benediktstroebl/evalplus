
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    left = 0
    for i in range(n//2):
        if lst[i] % 2 == 0:
            left = left + lst[i]
    return left + sum([x for x in lst if x % 2 != 0])

lst = [5, 8, 7, 1, 3, 3, 3, 3, 3, 3]
