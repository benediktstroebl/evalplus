
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # 1. find the index of all even positions
    idx = [i for i, x in enumerate(lst) if x % 2 == 0]
    # 2. loop through the even positions and find the sum of the odd elements
    sum = 0
    for i in idx:
        sum += lst[i] if i % 2 == 0 else lst[i - 1]
    return sum
