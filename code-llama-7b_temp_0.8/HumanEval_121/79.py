
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # your code here
    list_result = []
    for index, value in enumerate(lst):
        if (index + 1) % 2 == 0:
            if value % 2 != 0:
                list_result.append(value)
    return sum(list_result)

