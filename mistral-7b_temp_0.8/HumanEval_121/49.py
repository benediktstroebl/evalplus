
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Use a for loop to iterate through the list.
    # For each iteration, check if the element is even and if it is odd.
    # If it is even, then check if the element is odd. If it is odd, add it to a new list.
    # Return the sum of the elements in the new list.
    new_list = []
    for item in lst:
        if item % 2 == 0:
            if item % 2 != 0:
                new_list.append(item)
    return sum(new_list)

