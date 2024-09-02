
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Set up empty output list
    odd_sum = 0
    # Iterate through list
    for x in range(0, len(lst)-1):
        # If a list is even, add it to sum
        if x % 2 == 0:
            odd_sum += lst[x]
    return odd_sum
