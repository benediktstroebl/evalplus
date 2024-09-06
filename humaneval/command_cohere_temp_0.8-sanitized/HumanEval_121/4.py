def solution(lst):
    return sum(num for num in lst if num % 2 == 1 and (len(lst) - num) % 2 == 0)