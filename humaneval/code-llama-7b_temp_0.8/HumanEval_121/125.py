
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    even_index_list = [item for idx, item in enumerate(lst) if idx % 2 == 0]
    odd_index_list = [item for idx, item in enumerate(lst) if idx % 2 != 0]

    odd_index_list = [item for item in odd_index_list if item % 2 != 0]

    if len(even_index_list) == 0:
        return 0

    lst = []
    for idx in range(0, len(even_index_list)):
        lst.append(even_index_list[idx])
        lst.append(odd_index_list[idx])

    return sum(lst)
