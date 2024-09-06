
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] % 2 == 0:
            left = mid + 1
        else:
            right = mid
    return left * 2


test = [


[5, 8, 7, 1],
[3, 3, 3, 3, 3],
[30, 13, 24, 321],
[2, 1, 5, 2, 8],
[5, 8, 7, 1, 5],
[2, 1, 5, 2, 8, 7, 1],
[4, 6, 2, 5, 2, 8, 7],
[5, 8, 7, 1, 5, 2, 8],
[2, 1, 5, 2, 8, 7, 1, 5],
[5, 8, 7, 1, 5, 2, 8, 7],

]

for test_case in test:
    print(test_case)
    print(solution(test_case))
    































































































































































































