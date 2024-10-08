
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            if i+1 < len(lst) and lst[i+1] % 2 == 1:
                lst[i], lst[i+2] = lst[i+2], lst[i]
            elif i+1 == len(lst):
                break
    return lst