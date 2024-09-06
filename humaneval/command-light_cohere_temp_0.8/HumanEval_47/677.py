```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

# Test the median function
for _ in range(100):
    test_list = [random.randint(-10, 1000) for i in range(len(test_list))]
    assert median(test_list) == int((test_list[(len(test_list) // 2 - 1)] + test_list[(len(test_list) // 2)]  / 2))
```