```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This function uses a nested list comprehension that operates on a given array of integers (`arr`). In each iteration, it converts a number to a string and then to an integer array, sums up the digits, and checks whether this sum is greater than 0. Finally, it returns the number of elements that satisfy this condition.