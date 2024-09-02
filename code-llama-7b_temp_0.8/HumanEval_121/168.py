
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    #===============
    # Solution 1
    #===============
    # lst_even = list(filter(lambda num: num % 2 == 0, lst))
    #
    # def solution_helper(lst_even):
    #     ret = 0
    #     for i, num in enumerate(lst_even):
    #         if i % 2 == 0 and num % 2 != 0:
    #             ret += num
    #     return ret
    #
    # return solution_helper(lst_even)

    #===============
    # Solution 2
    #===============
    ret = 0
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 != 0:
            ret += num

    return ret


