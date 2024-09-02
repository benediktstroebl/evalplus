
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # 1st way
    # lst_even = [x for x in lst if x % 2 == 0]
    # lst_odd = [x for x in lst if x % 2!= 0]
    # return sum(lst_odd)
    
    # 2nd way
    return sum(x for x in lst if x % 2 == 1 and x % 2 == 0)
    
    # 3rd way
    # return sum(x if x % 2 == 1 and x % 2 == 0 else 0 for x in lst)
