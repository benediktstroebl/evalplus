
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    even_pos_nums = [num for idx, num in enumerate(lst) if idx % 2 == 0]
    odd_pos_nums = [num for idx, num in enumerate(lst) if idx % 2 != 0]
    odd_pos_nums_even = [num for idx, num in enumerate(odd_pos_nums) if num % 2 == 0]
    return sum(odd_pos_nums_even)

