
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
        odd_sum = lst[i]
        if i % 2 == 1:
            even_sum += odd_sum
        lst[i] = 0
    return even_sum
