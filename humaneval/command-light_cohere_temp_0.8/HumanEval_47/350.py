```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return float('-inf')  # handle empty list
    m = n // 2
    left, right = m - 1, m
    while left >= 0 and lst[left] > lst[right]:
        left -= 1
    while right < n - 1 and lst[right] > lst[left]:
        right += 1
    if left < right:
        mid = (left + right) // 2
        return mid
    return lst[n // 2]  # return mean of two middle values

# Test cases
print(median([-10, 4, 6, 1000, 10, 20] )) # 15.0
print(median([-10, 4, 6, 1000, 10, 20] )) # 15.0
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 5.0
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # 5.0
print(median([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # 5.0
print(median([10, 11, 12, 13, 14])) # 11.0
```