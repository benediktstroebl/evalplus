```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        mid1 = lst[(n//2) - 1]
        mid2 = lst[n//2]
        return (mid1 + mid2) / 2
    else:
        return lst[n//2]

# Test the function
for _ in range(20):
    test_lst = [i for i in range(100)]
    print(median(test_lst), end=' ')
```