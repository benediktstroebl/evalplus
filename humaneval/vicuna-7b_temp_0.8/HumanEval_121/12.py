
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    left, right = 1, 1
    sum = 0
    
    for i in range(1, len(lst)):
        if (lst[i] % 2 == 0):
            left = 2 * left + lst[i-1]
            right = 2 * right + lst[i]
            sum = max(sum, left - right)
            
    return sum

