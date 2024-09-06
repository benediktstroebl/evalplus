
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    def is_even(x):
        return x % 2 == 0
    
    def is_odd(x):
        return x % 2 != 0
    
    return sum(filter(lambda x: is_odd(i), filter(is_even, lst)))
