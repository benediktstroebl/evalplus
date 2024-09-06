def solution(lst):
    return sum(x for x in lst if x % 2 == 1 and (len(lst) - lst.index(x) - 1) % 2 == 0)