
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # O(n) time | O(n) space
    # if len(lst) % 2 != 0:
    #     lst.pop()
    # if len(lst) == 0:
    #     return 0
    # if len(lst) == 1:
    #     return lst[0]
    # elif len(lst) == 2:
    #     return lst[0]
    # sum = 0
    # for i in range(0, len(lst), 2):
    #     if lst[i] % 2 == 1:
    #         sum += lst[i]
    # return sum

    # O(n) time | O(1) space
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    sum = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 1:
            sum += lst[i]
    return sum

