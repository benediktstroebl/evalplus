
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Find all of the even positions
    # Filter out the odd elements
    # Sum the values in the list
    even_pos = [i for i, v in enumerate(lst) if i % 2 == 0]
    odd_elems = [ele for ele in lst if ele % 2 == 1]
    return sum(odd_elems[i] for i in even_pos)
