```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This solution uses a nested map-sum operation to determine whether the sum of digits of each number in the array is greater than zero. The sum operation then counts the number of elements that have a sum of digits greater than zero. The function returns this count.

This solution is efficient and does not require any additional imports. It can be directly executed with Python as a standalone function.