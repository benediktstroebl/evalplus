```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[(len(l) / 2) - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Test cases
for _ in range(20):
    test_list = [random.randint(-10, 1000) for i in range(2)]
    print(median(test_list))  # Output should be 5.0
```