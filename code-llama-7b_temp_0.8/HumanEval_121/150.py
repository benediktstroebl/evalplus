
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # count = 0
    # for x in range(0, len(lst), 2):
    #     if (lst[x] % 2 != 0):
    #         count += lst[x]
    # return count

    return sum([num for (pos, num) in enumerate(lst) if num % 2 != 0 and pos % 2 == 0])

