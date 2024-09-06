
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd = list(filter(lambda x: x % 2 != 0, lst))
    even = list(filter(lambda x: x % 2 == 0, lst))
    return sum([odd[i] for i, val in enumerate(even) if val % 2 != 0])
