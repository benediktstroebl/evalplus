
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    low, high = 0, len(lst)
    while low <= high:
        if not lst[low]:
            low += 1
        elif lst[low] % 2 == 0:
            low += 1
        else:
            high -= 1
    return low
