
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Your code here

    # Use zip() with a conditional to sum only the odd elements in even positions
    return sum(a for a,b in zip(lst, range(len(lst))) if b % 2!= 0)
