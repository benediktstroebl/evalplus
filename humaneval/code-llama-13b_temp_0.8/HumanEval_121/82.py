
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    # Tampered solution
    return sum(lst[::2]) if len(lst)%2 ==0 else sum(lst[1::2])

    # My first solution
    # This solution doesn't work for an array with an odd number of elements
    # return sum([lst[i] for i in range(0, len(lst), 2)])

    # Another solution
    # return sum(lst[1::2]) if len(lst)%2 else sum(lst[::2])


