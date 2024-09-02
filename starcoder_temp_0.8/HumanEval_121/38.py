
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    #sum of even elements
    sum_of_even = 0
    #sum of odd elements
    sum_of_odd = 0

    for i in range(0, len(lst)):
        if i % 2 == 0:
            sum_of_even = sum_of_even + lst[i]
        else:
            sum_of_odd = sum_of_odd + lst[i]
    return sum_of_odd
