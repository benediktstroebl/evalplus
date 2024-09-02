
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # check if the list is empty or not
    if not lst:
        return 0
    
    # get the odd elements in even positions
    odd_pos = [i for i in range(len(lst)) if not (lst[i] % 2 == 0)]
    
    # return the sum of all odd elements
    return sum(odd_pos)
