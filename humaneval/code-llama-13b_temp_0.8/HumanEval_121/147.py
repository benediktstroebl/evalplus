
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # lst = [int(x) for x in lst]
    # lst = list(filter(None, lst))
    new_lst = [lst[i] for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2 == 1]
    if len(new_lst) > 0:
        return sum(new_lst)
    else:
        return 0

