def solution(lst):
    return sum(num for ind, num in enumerate(lst) if ind % 2 == 1 and num % 2 == 1)