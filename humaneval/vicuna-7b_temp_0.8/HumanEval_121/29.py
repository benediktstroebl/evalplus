
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    num = 0
    for num in lst:
        if num % 2 == 1:
            num += num // 2
    return num

test = [1,2,3,4,5,6,7,8,9]
