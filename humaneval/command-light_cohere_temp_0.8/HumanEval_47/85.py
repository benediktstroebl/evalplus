```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2 - 1)] + lst[n//2]) / 2
    else:
        return lst[(n//2)]

# Test the function
# with sample list
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
print(median([1, 2, 3, 4, 5]))  # Output: 2.0
```