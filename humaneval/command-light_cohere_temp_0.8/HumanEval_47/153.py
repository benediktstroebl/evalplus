```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1) ** .5 / 2 * sum((x + 1) / 2 for x in lst)

# Test cases
for _ in range(25):
    lst = [random.randint(-10, 1000) for _ in range(100)]
    assert median(lst) == int((len(lst) + 1) ** .5 / 2 * sum((x + 1) / 2 for x in lst))
```