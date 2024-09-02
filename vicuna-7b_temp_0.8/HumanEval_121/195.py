
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    for i in range(len(lst)):
        if (lst[i] % 2 == 0 and lst[i] > 0):
            if lst[i-1] % 2 == 0:
                return lst[i-1] + lst[i]
            else:
                return lst[i]
    return 0

lst = input().split()
result = solution(lst)
