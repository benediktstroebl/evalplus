
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    i = 0
    total = 0
    for num in lst:
        if i % 2 == 0:
            if num % 2 != 0:
                total += num
        i += 1
    return total
