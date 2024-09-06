def solution(lst):
    odd_in_even = sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1)
    return odd_in_even