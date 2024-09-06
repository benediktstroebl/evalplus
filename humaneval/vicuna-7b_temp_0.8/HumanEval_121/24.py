
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd_lst = []
    for i in range(len(lst)-1):
        if lst[i] % 2 == 1 and odd_lst[-1] != lst[i]:
            odd_lst.append(lst[i])
        elif lst[i] % 2 == 1 and odd_lst[-1] == lst[i]:
            odd_lst[-1] = lst[i]
    return odd_lst[0]
