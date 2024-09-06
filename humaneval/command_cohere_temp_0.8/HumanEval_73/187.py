Here's a Python script with a self-contained function that solves the problem:
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
The function smallest_change calculates the minimum number of changes required to make the array palindromic for even and odd elements separately. Then it returns the minimum of these two counts, which will be the correct answer to the problem.