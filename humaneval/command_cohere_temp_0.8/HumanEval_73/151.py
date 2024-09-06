```python
def smallest_change(arr):
    odd, even = 0, 0
    for n in arr:
        if n == n[::-1]:
            even += 1
        else:
            odd += 1
    return min(odd, even)
```

The function `smallest_change()` calculates the number of odd changes (`odd`) and even changes (`even`) that would allow the reversed array to match the original. The minimum of `odd` and `even` is then returned as the solution.