
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd_sum = 0
    count = 0
    for index in range(len(lst)):
        if index % 2 == 0:
            if lst[index] % 2 != 0:
                odd_sum += lst[index]
                count += 1

    return odd_sum
