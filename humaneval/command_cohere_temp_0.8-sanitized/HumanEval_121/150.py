def solution(lst):
    return sum(el for el in lst if el % 2 == 1 and (len(lst) - lst.index(el)) % 2 == 0)