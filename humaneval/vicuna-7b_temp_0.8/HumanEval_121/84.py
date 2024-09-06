
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    if n%2 == 0:
        return 0
    else:
        x = [lst[i] for i in range(n//2)]
        y = [lst[i] for i in range(n//2,n)]
        return sum([x[i] for i in range(n//2) if x[i] % 2 == 1 and y[i] % 2 == 0])

print(solution(lst))