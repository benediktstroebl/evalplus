
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    # Solution 1
    # lst2 = [lst[i] for i in range(len(lst)) if lst[i] % 2 == 1 and i % 2 == 0]
    # return sum(lst2)
    
    # Solution 2
    sum_of_odd_even_pos = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1 and i % 2 == 0:
            sum_of_odd_even_pos += lst[i]
    return sum_of_odd_even_pos
