
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # 1. Get odd elements from a list using slicing [1::2]
    # 2. Sum of odd elements from a list

    odd_elements = lst[1::2]
    sum_of_elements = sum(odd_elements)

    return sum_of_elements
