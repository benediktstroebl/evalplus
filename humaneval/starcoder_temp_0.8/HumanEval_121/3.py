
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if len(lst) == 0:
        return 0
    even = []
    odd = []
    for i, item in enumerate(lst):
        if i % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    return sum(even)
