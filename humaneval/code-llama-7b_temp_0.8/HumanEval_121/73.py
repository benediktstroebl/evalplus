
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    lst.sort()
    a = 0
    b = 1
    x = 0
    while x < len(lst) and b < len(lst):
        if a % 2 == 1:
            x += 1
            a = lst[a]
            b = lst[b]
        else:
            a += 1
            b += 1
    return a

