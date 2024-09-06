def solution(lst):
    return sum(x for x in lst if x % 2 and lst.index(x) % 2 == 0)