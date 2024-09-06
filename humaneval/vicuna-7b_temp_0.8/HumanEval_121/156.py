
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
    
    # Check if there is an odd element in the list
    odd = next((x for x in lst if x % 2 == 1), None)
    
    # Check if the odd element is in an even position
    pos = next((i for i, x in enumerate(lst) if x % 2 == 0), None)
    if pos is None:
        return 0
    
    # Check if the odd element is in the current position
    if odd is None or odd in lst[pos:pos+2]:
        return lst[pos]
    else:
        return lst[pos] + solution(lst[pos+1:])
