def solution(lst):
    """Given a non-empty list of integers, returns the sum of all the odd elements that are in even positions."""
    return sum(x for x in lst if not_even(x, lst))
def not_even(x, lst):
    return x % 2 == 0