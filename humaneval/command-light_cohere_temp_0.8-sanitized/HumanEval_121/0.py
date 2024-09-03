def solution(lst):
    """Given a non-empty list of integers, returns the sum of all the odd elements that are in even positions."""
    return sum(n for n in lst if n%2==0 and n>=0)