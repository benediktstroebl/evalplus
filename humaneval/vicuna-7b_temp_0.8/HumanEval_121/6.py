
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    if n < 2:
        return 0
    elif n == 2:
        return lst[0] + lst[1]
    else:
        sum = 0
        for i in range(2, n):
            if i % 2 == 1:
                sum += lst[i]
        return sum

