
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum(lst[::2] + [lst[1] if lst[0] == lst[1] == lst[2] == lst[lst.index(lst[0])] else lst[0] for lst in sorted(lst, reverse=True))]
