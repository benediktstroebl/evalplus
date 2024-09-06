Here's a Python script with a self-contained function that solves the problem using Python:
```python
def smallest_change(arr):
    even, odd = 0, 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)
```

The function `smallest_change` calculates the minimum number of changes required to make the array palindromic by counting the number of even and odd elements in the array. The difference between these counts represents the minimum number of changes required to make the array palindromic. Ultimately, it returns the smaller count between `even` and `odd` variables.