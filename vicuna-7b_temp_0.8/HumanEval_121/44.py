
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Read in the input list
    n = len(lst)
    # Initialize a variable to store the sum
    sum = 0
    # For each element in the list, check if it is odd and if it is in an even position
    for i in range(n):
        if lst[i] % 2 == 1 and lst[i] // 2 == 0:
            # If the element is odd and in an even position, add it to the sum
            sum += lst[i]
    return sum
