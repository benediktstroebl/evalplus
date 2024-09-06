
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Check if the list is empty
    if not lst:
        return 0
    
    # Check if the list is a single element
    if len(lst) == 1:
        return lst[0]
    
    # Check if the sum of all the elements is 0
    total = sum(lst)
    if total == 0:
        return 0
    
    # Check if the sum of all the elements is greater than 1
    if total > 1:
        return total
    
    # Check if the sum of all the elements is 0 or 1
    # Return the first odd element
    odd = [i for i in lst if i % 2 == 1]
    return sum(odd)
