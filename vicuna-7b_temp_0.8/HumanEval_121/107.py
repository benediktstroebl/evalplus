
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

    # Initialize a variable for the sum
    sum = 0

    # Iterate over the elements of the list
    for num in lst:
        # Check if the current element is odd
        if num % 2 == 1:
            # Add the current element to the sum
            sum += num

    return sum
