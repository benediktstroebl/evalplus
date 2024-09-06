
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Use the window of 2 to find the first odd element in the even position
    if lst[0] % 2 != 0:
        return lst[0]
    # If there is no odd element in the first position, return 0
    if len(lst) == 1:
        return 0
    # The odd element is the first one after the window of 2
    i = 1
    odd = 0
    while lst[i] % 2 == 0:
        i += 1
    # The sum of the odd elements is the sum of all the odd elements after the first one
    odd += lst[i]
    return odd
