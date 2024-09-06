
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # make sure lst is not empty list
    if len(lst) == 0:
        return None

    # sum of odd numbers in even positions
    sum_of_odd_numbers = 0

    # iterate through lst, check if number is odd
    for i in range(0, len(lst)):
        # if list number is odd and its position is even
        if lst[i] % 2 == 1 and i % 2 == 0:
            sum_of_odd_numbers += lst[i]

    return sum_of_odd_numbers

