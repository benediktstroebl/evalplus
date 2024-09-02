
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0

    def is_odd(n):
        return n % 2 == 1

    def is_even(n):
        return n % 2 == 0

    def get_sum(lst):
        return sum(lst)

    def filter_odd(lst):
        return list(filter(is_odd, lst))

    def filter_even(lst):
        return list(filter(is_even, lst))

    return get_sum(filter_odd(filter_even(lst)))

