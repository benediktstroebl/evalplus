
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    even_sum = 0
    for i in range(n):
        odd_sum = 0
        for j in range(i+1, n):
            odd_sum += lst[j]
        odd_sum += lst[i]
        even_sum += odd_sum
    return even_sum
