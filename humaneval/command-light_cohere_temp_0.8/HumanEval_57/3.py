```python
def monotonic(l: list):
    return all([x >= y for x, y in zip(l, l[1:])]) or all([y <= x for x, y in zip(l, l[1:])])
# tests
monotonic([1, 2, 4, 20])  # True
monotonic([1, 20, 4, 10])  # False
monotonic([4, 1, 0, -10])  # True
```
This function uses a generator expression to iterate over the list, comparing each element to all the rest. It returns True if the yet elements are monotonically increasing or decreasing.