```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test the function with a list of numbers
test_list = [10, 20, 40, 30, 60, 70, 80, 90, 100, 120]
print(median(test_list))  # Output should be 50.0
```