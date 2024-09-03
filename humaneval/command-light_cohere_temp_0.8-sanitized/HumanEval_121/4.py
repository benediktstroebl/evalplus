def solution(lst):
    """Given a list of integers, return the sum of all of the odd elements that are in even positions."""
    sum_odd = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            continue
        sum_odd += lst[i]
    return sum_odd