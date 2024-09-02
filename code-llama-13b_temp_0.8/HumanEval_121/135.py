
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    lst2 = []
    for idx, val in enumerate(lst):
        if idx%2 == 0:
            lst2.append(val)
    lst3 = []
    for val in lst2:
        if val%2 != 0:
            lst3.append(val)
    return sum(lst3)
