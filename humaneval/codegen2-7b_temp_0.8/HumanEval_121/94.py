
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    sum_of_odd = 0
    for index, element in enumerate(lst):
        if index % 2!= 0:
            sum_of_odd += element
    return sum_of_odd
