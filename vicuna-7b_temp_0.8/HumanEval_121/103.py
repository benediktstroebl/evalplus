
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    i, j = 0, 0
    while i < len(lst)-1:
        if(lst[i] % 2 == 0 and lst[j] % 2 != 0):
            j += 1
        elif(lst[i] % 2 != 0 and lst[j] % 2 == 0):
            i += 1
        elif(lst[i] % 2 != 0 and lst[j] % 2 != 0):
            return -1
    return 0
