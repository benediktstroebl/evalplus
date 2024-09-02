
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    lst2 = lst[1::2]
    lst3 = lst[::2]
    output = 0
    for x in range(len(lst2)):
        if lst2[x] % 2 == 1:
            output += lst2[x]
    return output
