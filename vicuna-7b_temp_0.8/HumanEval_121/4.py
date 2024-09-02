
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    odd_pos = 0
    for i in range(n):
        if(lst[i]%2 == 0):
            odd_pos += lst[i]
    return odd_pos


test_cases = [
    ( [5, 8, 7, 1], 12),
    ( [3, 3, 3, 3, 3], 9),
    ( [30, 13, 24, 321], 0),
]

for test_case in test_cases:
    result = solution(test_case[0])
    print(test_case[0] + " ==> " + str(result))