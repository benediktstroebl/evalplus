
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # your code here

    lst = [0] * len(lst)
    lst[::2] = lst[::2] + lst[1::2]
    lst[::2] = [x if x%2 == 1 else 0 for x in lst[::2]]
    return sum(lst)
