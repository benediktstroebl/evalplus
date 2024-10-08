
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    for i in range(n):
        if i % 2 == 1:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    for i in range(n-1, -1, -1):
        if i % 2 == 1:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    result = []
    for num in lst:
        if num % 2 == 1:
            result.append(num)
    return sum(result)
