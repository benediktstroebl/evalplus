
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    
    odd_sum = 0
    for i in range(0, len(lst)):
        if lst[i] % 2!= 0:
            odd_sum += lst[i]
            i += 1
            continue
        else:
            i += 1
            continue
    
    return odd_sum

