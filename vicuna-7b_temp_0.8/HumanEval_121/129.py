
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0
    n = len(lst)
    for i in range(n):
        if i % 2 == 0:
            sum = 0
            for j in range(i+1, n):
                sum += lst[j]
            lst[i:n] = [sum]
    return sum(lst)
