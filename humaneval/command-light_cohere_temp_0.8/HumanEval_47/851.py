```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
# Test cases
median([3, 1, 2, 4, 5]) # 3
median([-10, 4, 6, 1000, 10, 20]) # 15.0
median([1, 2, 3, 4, 5, 6]) # 3
median([-2, -1, 4, 5, 6]) # Assuming order matters in this case
median([10, 20, 30, 40]) # 40
```