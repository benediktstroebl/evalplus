
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Sum all of the values in the even positions.
    even_sum = sum(x for i, x in enumerate(lst) if i % 2 == 0)
    return even_sum
