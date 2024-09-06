
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Check if the list is empty or not
    if not lst:
        return 0

    # Keep track of the sum of the odd elements in the odd positions
    odd_sum = 0

    # Iterate through the list
    for i in range(len(lst)):
        # Check if the element is odd or not
        if lst[i] % 2 == 1:
            # If it is odd, increment the odd_sum variable
            odd_sum += lst[i]

    # If the odd_sum variable has a value, return its sum
    return odd_sum
