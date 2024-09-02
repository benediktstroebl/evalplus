
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    my_list = []
    for position in range(len(lst)):
        if lst[position] % 2 == 1:
            my_list.append(lst[position])
    return sum(my_list)

