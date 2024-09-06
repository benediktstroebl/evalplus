
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0] if lst[0]%2 == 0 else 0
    else:
        lst = lst[::2]
        return sum([item for item in lst if item%2 != 0])

    #return sum([item for item in lst if item%2 != 0 and lst.index(item)%2==0])














