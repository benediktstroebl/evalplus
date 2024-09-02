
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0
    i = 0
    even_sum = 0
    for j in range(1, len(lst)):
        if lst[j] % 2 == 0:
            even_sum += lst[j]
        else:
            odd_sum += lst[j]
            even_sum += odd_sum
    return even_sum
