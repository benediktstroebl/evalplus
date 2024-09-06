
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
    
    # Find the index of the first odd element
    odd_index = 0
    for i in range(1, len(lst)):
        if lst[i] % 2 != 0:
            odd_index = i
            break
    
    # Initialize the sum
    sum = 0
    
    # Find the index of the first even element greater than the first odd element
    if odd_index == 0:
        odd_index = 1
    while odd_index < len(lst) and lst[odd_index] % 2 == 0:
        odd_index += 1
    
    # Add the sum of the odd elements to the sum
    for i in range(odd_index, len(lst)):
        sum += lst[i]
    
    return sum