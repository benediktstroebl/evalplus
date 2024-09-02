
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
    elif n == 1:
        return lst[0]
    elif n % 2 == 0:
        return sum(lst[i] for i in range(n))
    else:
        left = sum(lst[i] for i in range(n))
        right = sum(lst[i] for i in range(n-1))
        return left + right + lst[n-1]