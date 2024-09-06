
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

    # If the list is not empty, it means we can find an odd element in the list
    # and therefore we can return the sum of all the odd elements in the list
    return sum(lst[::2] + [lst[1] if lst[0] % 2 == 0 else lst[0] for _ in range(len(lst)-1)])
