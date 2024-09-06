```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test the function with a range of inputs
for i in range(0, 30):
    if median(range(i, i+5)) == i+2:
        print(f"{i+2} is median")
    else:
        print(f"{i+2} is not median")
```