def solution(lst):
    even = 0
    odd = 0
    sum_odd = 0
    while odd < len(lst):
      if (odd + 1) % 2 == 0:
        sum_odd += lst[odd]
        odd += 2
      else:
        even += 2
        odd += 1
    return sum_odd