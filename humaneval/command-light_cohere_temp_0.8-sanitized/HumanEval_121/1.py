def solution(lst):
    """Given a non-empty list of integers, returns the sum of all odd elements in even positions."""
    return sum(x for x in lst if x%2 != 0 and (x < 0) == (lst[0] < 0))