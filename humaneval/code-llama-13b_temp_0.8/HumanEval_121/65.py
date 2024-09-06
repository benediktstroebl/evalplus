
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    if not lst:
        return 0
    
    return sum(item for index, item in enumerate(lst) if item % 2 and index % 2)
    # easy solution
    # return sum(lst[1::2]) if len(lst) > 1 else 0

