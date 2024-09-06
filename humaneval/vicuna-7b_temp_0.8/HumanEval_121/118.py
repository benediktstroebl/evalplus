
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    if n == 0:
        return 0
    odd_pos = [0] * n
    odd_sum = [0] * n
    for i in range(n):
        odd_pos[i] = 2*(i+1) % 2 == 1
        odd_sum[i] = lst[odd_pos[i]]
    for i in range(n-1, -1, -1):
        if odd_pos[i] < odd_pos[i-1]:
            odd_pos[i] += 2
            odd_sum[i] += odd_sum[i-1]
            odd_sum[i-1] = 0
    return odd_sum[-1]
