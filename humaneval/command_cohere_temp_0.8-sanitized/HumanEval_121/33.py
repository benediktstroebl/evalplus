def solution(lst):
    odd_in_even = sum(x for x in lst if x % 2 and (len(lst) - x) % 2 == 0)
    return odd_in_even