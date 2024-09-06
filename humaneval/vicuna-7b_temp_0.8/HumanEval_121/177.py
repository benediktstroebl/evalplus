
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    i, j = 0, 0
    for num in lst:
        if num % 2 == 1:
            odd = num // 2
            while j < i and odd * 2 <= lst[j]:
                lst[j] = lst[j] + odd * 2
                j += 1
            j += 1
    return lst