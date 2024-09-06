
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    sum_odd_even = 0
    lst_len = len(lst)
    for i in range(lst_len):
        if i%2 != 0 and lst[i]%2 != 0:
            sum_odd_even += lst[i]
    return sum_odd_even
