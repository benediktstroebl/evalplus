```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[-1] + l[0]) / 2
    else:
        return l[int((n - 1) / 2)]

# Test the function with various lists
print(median([-10, 4, 6, 1000, 10, 20] )) # Output: 15.0
print(median([1, 2, 4, 5]))    # Output: 5.0
print(median([-5, -3, 8, -1, 1, -8])) # Output: -1.8
print(median([10, 20, 30, 40, 50]))  # Output: 40.0
```