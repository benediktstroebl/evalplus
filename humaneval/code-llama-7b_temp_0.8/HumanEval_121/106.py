
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd = lambda x: x % 2 == 1
    even = lambda x: x % 2 == 0
    odd_elements_even_positions = filter(odd, lst)
    filter_even_elements = filter(even, odd_elements_even_positions)
    return sum(filter_even_elements)
    
