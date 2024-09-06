
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if len(lst) == 0:
        return 0

    lst_odd = [lst[i] for i in range(0, len(lst)) if i % 2 == 1]
    lst_even = [lst[i] for i in range(0, len(lst)) if i % 2 == 0]

    return sum(lst_odd)

