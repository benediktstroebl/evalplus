
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    i = 0
    summ = 0
    while i < len(lst):
        if lst[i] % 2 == 1:
            summ += lst[i]
        i += 1
    return summ

