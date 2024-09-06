```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[-1] + l[0]) / 2
    else:
        return l[int((n-1) / 2)]

# Test cases
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
print(median([-20, -10, -15, 25]))    # Output: -15
print(median([10, 20, -10, -30, -40]))  # Output: -40
print(median([1, 2, 3, 4, 5]))       # Output: 3
print(median([10, -10, 40, 20]))      # Output: 10
```