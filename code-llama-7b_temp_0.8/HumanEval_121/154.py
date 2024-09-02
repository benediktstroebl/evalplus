
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    #return sum(num for num in lst[::2] if num % 2)
    return sum(num for i, num in enumerate(lst) if i % 2 and num % 2)
